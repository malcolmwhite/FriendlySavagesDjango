from django.template import RequestContext, loader
from django.http import HttpResponse

from lyrics.models import Album, Song


def index(request):
    songs_list = Song.objects.all()
    template = loader.get_template('lyrics/index.html')
    context = RequestContext(request, {
        'songs_list': songs_list,
    })
    return HttpResponse(template.render(context))


def song_detail(request, song_id):
    song = Song.objects.get(song_id)
    template = loader.get_template('lyrics/song_detail.html')
    context = RequestContext(request, {
        'song': song,
    })
    return HttpResponse(template.render(context))


def album_detail(request, album_id):
    album = Album.objects.get(album_id)
    template = loader.get_template('lyrics/album_detail.html')
    context = RequestContext(request, {
        'album': album
    })

    return HttpResponse(template.render(context))