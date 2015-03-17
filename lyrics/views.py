from lyrics.models import Album
from core.views import generic_view


def album_detail(request, album_id, **data):
    data['album'] = Album.albums.get(pk=album_id)
    return apply(generic_view, (request,), data)

