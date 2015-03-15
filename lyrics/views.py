from django.template import RequestContext, loader
from django.http import HttpResponse

from lyrics.models import Album, Song


def index(request):
    template = loader.get_template('lyrics/index.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))


def song_detail(request, song_id):
    song = Song.objects.get(pk=song_id)
    template = loader.get_template('lyrics/song_detail.html')
    context = RequestContext(request, {
        'song': song,
    })
    return HttpResponse(template.render(context))


def album_detail(request, album_id):
    album = Album.albums.get(pk=album_id)
    template = loader.get_template('lyrics/album_detail.html')
    context = RequestContext(request, {
        'album': album,
    })

    return HttpResponse(template.render(context))