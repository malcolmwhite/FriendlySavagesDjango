from lyrics.models import Album, Song


def album_list(request):
    albums = Album.albums.all()
    return {'album_list': albums}

def soundbar_playlist(request):
    soundbar_playlist = Song.objects.filter(in_soundbar_playlist=True)
    return {'soundbar_playlist': soundbar_playlist}