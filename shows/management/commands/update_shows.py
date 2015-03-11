import urllib2
import json

from django.core.management.base import BaseCommand

from shows.models import ShowListing


class Command(BaseCommand):
    help = 'Updates all show listings and related artists and venues'

    def handle(self, *args, **options):
        url = \
            'http://api.bandsintown.com/artists/Friendly%20Savages/events.json?api_version=2.0&app_id=SOUNDLY&date=all'
        serialized_data = urllib2.urlopen(url).read()
        packed_shows = json.loads(serialized_data)
        for packed_show in packed_shows:
            self.unpack_show(packed_show)


    @staticmethod
    def unpack_show(packed_show):
        try:
            title = packed_show[u"title"]
            datetime = packed_show[u"datetime"]
            facebook_rsvp_url = packed_show[u"facebook_rsvp_url"]
            unpacked_show = ShowListing.shows.get(title=title, datetime=datetime, facebook_rsvp_url=facebook_rsvp_url)
        except ShowListing.DoesNotExist:
            unpacked_show = ShowListing.shows.create_show(packed_show)
            unpacked_show.save()
        return unpacked_show