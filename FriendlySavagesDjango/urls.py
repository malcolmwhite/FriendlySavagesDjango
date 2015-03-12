from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^shows/', include('shows.urls', namespace="shows")),
                       url(r'^/?$', include('home.urls', namespace="home")),
                       url(r'^lyrics/', include('lyrics.urls', namespace="lyrics")),
                       url(r'^videos/', include('videos.urls', namespace="videos")),
                       url(r'^admin/', include(admin.site.urls)),
                       )
