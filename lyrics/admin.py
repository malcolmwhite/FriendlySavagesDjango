from django.contrib import admin

from lyrics.models import Album, Song


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass

