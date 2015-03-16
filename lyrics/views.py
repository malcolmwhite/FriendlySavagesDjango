from lyrics.models import Album, Song
from core.views import generic_view


# def album_list_view(request, **data):
#     data['albums'] = Album.albums.all()
#     return apply(generic_view, (request,), data)


def song_detail(request, song_id, **data):
    data['song'] = Song.objects.get(pk=song_id)
    return apply(generic_view, (request,), data)


def album_detail(request, album_id, **data):
    data['album'] = Album.albums.get(pk=album_id)
    return apply(generic_view, (request,), data)

