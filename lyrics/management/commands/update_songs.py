import urllib2
import json

from django.core.management.base import BaseCommand

from lyrics.models import Song, Album
from shows.models import Artist


class Command(BaseCommand):
    help = 'Updates all show listings and related artists and venues'

    def handle(self, *args, **options):
        url = \
            'https://api.spotify.com/v1/artists/3Ig26ddcKT3uUPpvLjzMAw/albums'
        serialized_albums = urllib2.urlopen(url).read()
        album_metadatas = json.loads(serialized_albums)[u"items"]
        for album_metadata in album_metadatas:
            self.get_and_unpack_album(album_metadata)


    @staticmethod
    def unpack_song(packed_song, album):
        title = packed_song[u"name"]
        number = packed_song[u"track_number"]
        duration_ms = packed_song[u"duration_ms"]
        try:
            unpacked_song = Song.objects.get(album=album, number=number)
        except Song.DoesNotExist:
            unpacked_song = Song.objects.create(album=album, number=number, title=title,
                                                milliseconds=duration_ms)
            unpacked_song.save()
        return unpacked_song


    def get_and_unpack_album(self, album_metadata):
        album_href = album_metadata[u"href"]
        serialized_album = urllib2.urlopen(album_href).read()
        packed_album = json.loads(serialized_album)
        try:
            name = packed_album[u"name"]
            spotify_url = packed_album[u"spotify_url"]
            unpacked_album = Album.objects.get(name=name, spotify_url=spotify_url, spotify_href=album_href)
        except Album.DoesNotExist:
            unpacked_album = Album.albums.create_album(packed_album)
            unpacked_album.save()
        packed_songs = packed_album[u"tracks"]
        songs = [self.unpack_song(packed_song, unpacked_album) for packed_song in packed_songs]
        return unpacked_album
