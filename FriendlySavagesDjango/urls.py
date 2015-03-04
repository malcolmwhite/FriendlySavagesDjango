from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'home.views.home', name='home'),
    url(r'^/$', 'home.views.home', name='home'),
    url(r'^shows/', include('shows.urls')),
    url(r'^shows/(?P<show_id>\d+)/$', 'shows.views.detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_shows/$', 'shows.views.get_shows'),
)
