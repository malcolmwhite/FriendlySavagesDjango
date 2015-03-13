from django.db import models

from shows.models import Artist


def content_file_name(instance, filename):
    return '/'.join(['cover_art', instance.title, filename])


class AlbumManager(models.Manager):
    def create_album(self, packed_album):
        name = packed_album[u"name"]
        packed_artists = packed_album[u"artists"]
        unpacked_artists = [Artist.artists.create_artist_from_spotify(packed_artist) for packed_artist in
                            packed_artists]
        release_date = packed_album[u"release_date"]
        images = packed_album[u"images"]
        cover, cover_thumb = self.get_cover_and_thumb(images)
        album_type = packed_album[u"album_type"]
        spotify_href = packed_album[u"href"]
        spotify_url = packed_album[u"external_urls"]["spotify"]
        try:
            album = self.get(name=name, spotify_url=spotify_url, spotify_href=spotify_href)
        except Album.DoesNotExist:
            album = self.create(name=name, cover_url=cover, cover_thumb_url=cover_thumb, album_type=album_type,
                                spotify_href=spotify_href, spotify_url=spotify_url)
            for artist in unpacked_artists:
                album.artists.add(artist)
            album.save()

        return album

    @staticmethod
    def get_cover_and_thumb(images):
        return images[1], images[-1]


class Album(models.Model):
    name = models.CharField(max_length=100)
    artists = models.ManyToManyField(Artist)
    release_date = models.DateField(null=True)
    spotify_url = models.URLField()
    spotify_href = models.URLField()
    cover_url = models.URLField(null=True)
    cover_thumb_url = models.URLField(null=True)
    album_type = models.CharField(max_length=100)
    albums = AlbumManager()

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'spotify_url', 'spotify_href')


class Song(models.Model):
    album = models.ForeignKey(Album, related_name='songs')
    number = models.IntegerField()
    title = models.CharField(max_length=100)
    lyrics = models.TextField()
    milliseconds = models.IntegerField()

    def __unicode__(self):
        return '%s (%d) %s' % (self.album.name, self.number, self.title)

    class Meta:
        ordering = ('number',)
        unique_together = ('album', 'number',)