from django.db import models
from shows.models import Artist


def content_file_name(instance, filename):
    return '/'.join(['cover_art', instance.title, filename])


class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist)
    release_date = models.DateField()
    cover_art = models.FileField(upload_to=content_file_name)
    spotify_url = models.URLField()
    spotify_href = models.URLField()
    images = models.FileField(many=True)
    album_type = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s: %s' % (self.artist.name, self.name)

    class Meta:
        unique_together = ('name', 'artist', 'spotify_url', 'spotify_href')


class Song(models.Model):
    album = models.ForeignKey(Album, related_name='tracks')
    number = models.IntegerField()
    title = models.CharField(max_length=100)
    lyrics = models.TextField()
    minutes = models.IntegerField()
    seconds = models.IntegerField()

    def __unicode__(self):
        return '%s (%d) %s' % (self.album.title, self.number, self.title)

    class Meta:
        ordering = ('number',)
        unique_together = ('album', 'number',)