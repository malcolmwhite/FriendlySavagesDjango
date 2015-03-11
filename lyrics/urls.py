from django.conf.urls import patterns, url

from lyrics import views

urlpatterns = patterns('',
                       # ex: /lyrics/
                       url(r'^$', views.index, name='index'),
                       # ex: /lyrics/1/
                       url(r'^albums/(?P<album_id>\d+)/$', views.album_detail, name='album_detail'),
                       url(r'^songs/(?P<song_id>\d+)/$', views.song_detail, name='song_detail'),
                       )