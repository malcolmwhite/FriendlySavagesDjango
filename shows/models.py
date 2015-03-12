from django.db import models
import urllib2
import json


class VenueManager(models.Manager):
    def create_venue(self,  packed_venue):
        name = packed_venue[u"name"]
        city = packed_venue[u"city"]
        region = packed_venue[u"region"]
        latitude = packed_venue[u"latitude"]
        longitude = packed_venue[u"longitude"]

        try:
            venue = self.get(name=name, latitude=latitude, longitude=longitude)
        except Venue.DoesNotExist:
            venue = self.create(name=name, city=city, region=region, latitude=latitude, longitude=longitude)
            venue.save()
        return venue


class Venue(models.Model):
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    venues = VenueManager()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class ArtistManager(models.Manager):
    def create_artist_from_bandcamp(self,  packed_artist):
        name = packed_artist[u"name"]
        image_url = packed_artist[u"image_url"]
        thumb_url = packed_artist[u"thumb_url"]
        facebook_tour_dates_url = packed_artist[u"facebook_tour_dates_url"]
        mbid = packed_artist[u"mbid"]
        # upcoming_events_count = packed_artist[u"upcoming_events_count"]
        try:
            artist = self.get(name=name, facebook_tour_dates_url=facebook_tour_dates_url)
        except Artist.DoesNotExist:
            artist = self.create(name=name, image_url=image_url, thumb_url=thumb_url,
                                 facebook_tour_dates_url=facebook_tour_dates_url, mbid=mbid)
            artist.save()
        return artist

    def create_artist_from_spotify(self,  incomplete_packed_artist):
        name = incomplete_packed_artist[u"name"]
        href = incomplete_packed_artist[u"href"]
        serialized_data = urllib2.urlopen(href).read()
        complete_packed_artist = json.loads(serialized_data)
        images = complete_packed_artist[u"images"]
        image_url = images[0][u"url"]
        thumb_url = images[-1][u"url"]
        try:
            artist = self.get(name=name)
        except Artist.DoesNotExist:
            artist = self.create(name=name, image_url=image_url, thumb_url=thumb_url,
                                 facebook_tour_dates_url=None, mbid=None)
            artist.save()
        return artist


class Artist(models.Model):
    name = models.CharField(max_length=40)
    image_url = models.URLField()
    thumb_url = models.URLField()
    facebook_tour_dates_url = models.URLField(null=True)
    mbid = models.CharField(max_length=40, null=True)
    artists = ArtistManager()

    class Meta:
        unique_together = ('name',)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class ShowListingManager(models.Manager):
    def create_show(self, packed_show):
        title = packed_show[u"title"]
        datetime = packed_show[u"datetime"]
        formatted_datetime = packed_show[u"formatted_datetime"]
        formatted_location = packed_show[u"formatted_location"]
        ticket_url = packed_show[u"ticket_url"]
        ticket_type = packed_show[u"ticket_type"]
        ticket_status = packed_show[u"ticket_status"]
        on_sale_datetime = packed_show[u"on_sale_datetime"]
        facebook_rsvp_url = packed_show[u"facebook_rsvp_url"]
        description = packed_show[u"description"]
        packed_artists = packed_show[u"artists"]
        artists = [Artist.artists.create_artist_from_bandcamp(artist) for artist in packed_artists]
        venue = Venue.venues.create_venue(packed_show[u"venue"])
        show = self.create(title=title, datetime=datetime, formatted_datetime=formatted_datetime,
                           formatted_location=formatted_location, ticket_url=ticket_url, ticket_type=ticket_type,
                           ticket_status=ticket_status, on_sale_datetime=on_sale_datetime,
                           facebook_rsvp_url=facebook_rsvp_url, description=description, venue=venue)
        for artist in artists:
            show.artists.add(artist)
        return show


class ShowListing(models.Model):
    title = models.CharField(max_length=400)
    datetime = models.DateTimeField('date and time of show')
    formatted_datetime = models.CharField(max_length=200)
    formatted_location = models.CharField(max_length=40)
    ticket_url = models.URLField(null=True)
    ticket_type = models.CharField(max_length=40, null=True)
    ticket_status = models.CharField(max_length=40)
    on_sale_datetime = models.DateTimeField(null=True)
    facebook_rsvp_url = models.URLField()
    description = models.CharField(max_length=200, null=True)
    artists = models.ManyToManyField(Artist, null=True)
    venue = models.ForeignKey(Venue, null=True)
    shows = ShowListingManager()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ('datetime',)
        unique_together = ('title', 'datetime', 'facebook_rsvp_url')

