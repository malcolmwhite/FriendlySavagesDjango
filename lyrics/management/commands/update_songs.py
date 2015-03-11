import urllib2
import json

from django.core.management.base import BaseCommand

from lyrics.models import Song, Album


class Command(BaseCommand):
    help = 'Updates all show listings and related artists and venues'

    def handle(self, *args, **options):
        url = \
            'https://api.spotify.com/v1/artists/3Ig26ddcKT3uUPpvLjzMAw/albums'
        serialized_albums = urllib2.urlopen(url).read()
        packed_albums = json.loads(serialized_albums)
        for packed_album in packed_albums:
            self.get_and_unpack_album(packed_album)


    @staticmethod
    def get_and_unpack_album(packed_album):

        try:
            title = packed_show[u"title"]
            datetime = packed_show[u"datetime"]
            facebook_rsvp_url = packed_show[u"facebook_rsvp_url"]
            unpacked_show = ShowListing.shows.get(title=title, datetime=datetime, facebook_rsvp_url=facebook_rsvp_url)
        except ShowListing.DoesNotExist:
            unpacked_show = ShowListing.shows.create_show(packed_show)
            unpacked_show.save()
        return unpacked_show

    @staticmethod
    def unpack_song(packed_show):
        try:
            title = packed_show[u"title"]
            datetime = packed_show[u"datetime"]
            facebook_rsvp_url = packed_show[u"facebook_rsvp_url"]
            unpacked_show = ShowListing.shows.get(title=title, datetime=datetime, facebook_rsvp_url=facebook_rsvp_url)
        except ShowListing.DoesNotExist:
            unpacked_show = ShowListing.shows.create_show(packed_show)
            unpacked_show.save()
        return unpacked_show