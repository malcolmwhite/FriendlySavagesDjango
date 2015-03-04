from django.db import models


class Venue(models.Model):
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class ShowListing(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=40)
    datetime = models.DateTimeField('date and time of show')
    formatted_datetime = models.CharField(max_length=200)
    formatted_location = models.CharField(max_length=40)
    ticket_url= models.URLField()
    ticket_type = models.CharField(max_length=40)
    ticket_status = models.CharField(max_length=40)
    on_sale_datetime = models.DateTimeField('date and time of show')
    facebook_rsvp_url= models.URLField()
    description = models.CharField(max_length=200)
    artists = models.ManyToManyField('Artist')
    venue = models.ForeignKey('Venue')

    def __str__(self):
        return self.venue.city + ", " + self.venue.state + ": " + str(self.date_and_time.month) + " / " \
               + str(self.date_and_time.day)


class Artist(models.Model):
    name = models.CharField(max_length=40)
    image_url= models.URLField()
    thumb_url= models.URLField()
    facebook_tour_dates_url= models.URLField()
    mbid = models.CharField(max_length=40)
    upcoming_events_count = models.IntegerField()
