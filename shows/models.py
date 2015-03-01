from django.db import models


class Venue(models.Model):
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class ShowListing(models.Model):
    date_and_time = models.DateTimeField('date and time of show')
    venue = models.ForeignKey('Venue')
    opener = models.CharField(max_length=40)
    ticket_url = models.CharField(max_length=100)
    other_info = models.CharField(max_length=200)
    sold_out = models.BooleanField(default=False)

    def __str__(self):
        return self.venue.city + ", " + self.venue.state + ": " + str(self.date_and_time.month) + " / " \
               + str(self.date_and_time.day)