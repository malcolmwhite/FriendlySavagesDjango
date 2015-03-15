from lyrics.models import Album


def album_list(request):
    albums = Album.albums.all()
    return {'album_list': albums}