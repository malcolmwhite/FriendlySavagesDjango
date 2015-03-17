from django.conf.urls import patterns, url

from lyrics import views
from lyrics.models import Album
from core.views import generic_view

album_template_info = {
    'base_template': 'base.html',
    'active_link': '#main_link',
    'template': 'lyrics/album_list.html',
    'albums': Album.albums.all()
}

album_detail_template_info = {
    'base_template': 'base.html',
    'active_link': '#main_link',
    'template': 'lyrics/album_detail.html',
}


urlpatterns = patterns('',
                       # ex: /lyrics/
                       url(r'^$', generic_view, album_template_info, name='album_list'),
                       # ex: /lyrics/1/
                       url(r'^albums/(?P<album_id>\d+)/$', views.album_detail, album_detail_template_info, name='album_detail'),
                       # url(r'^songs/(?P<song_id>\d+)/$', views.song_detail, name='song_detail'),
                       )