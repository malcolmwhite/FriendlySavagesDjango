from django.db import models
from shows.models import Artist


def content_file_name(instance, filename):
    return '/'.join(['cover_art', instance.title, filename])


class AlbumManager(models.Manager):
    def create_album(self,  packed_album):
        name = packed_album[u"name"]
        packed_artists = packed_album[u"artists"]
        artists = [Artist.artists.create_artist_from_spotify(artist) for artist in packed_artists]
        release_date = packed_album[u"release_date"]
        images = packed_album[u"images"]
        album_type = packed_album[u"album_type"]
        spotify_href = packed_album[u"href"]
        spotify_url = packed_album[u"external_urls"]["spotify"]
        try:
            album = self.get(name=name, spotify_url=spotify_url, spotify_href=spotify_href)
        except Artist.DoesNotExist:
            album = self.create(name=name, images=images, album_type=album_type,
                                 spotify_href=spotify_href, spotify_url=spotify_url)
            album.save()

        for artist in artists:
            album.artists.add(artist)

        return album


class Album(models.Model):
    name = models.CharField(max_length=100)
    primary_artist = models.ForeignKey(Artist, null=True)
    artists = models.ManyToManyField(Artist)
    release_date = models.DateField()
    spotify_url = models.URLField()
    spotify_href = models.URLField()
    images = models.FileField(many=True)
    album_type = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s: %s' % (self.primary_artist.name, self.name)

    class Meta:
        unique_together = ('name', 'spotify_url', 'spotify_href')


class Song(models.Model):
    album = models.ForeignKey(Album, related_name='tracks')
    number = models.IntegerField()
    title = models.CharField(max_length=100)
    lyrics = models.TextField()
    milliseconds = models.IntegerField()

    def __unicode__(self):
        return '%s (%d) %s' % (self.album.title, self.number, self.title)

    class Meta:
        ordering = ('number',)
        unique_together = ('album', 'number',)