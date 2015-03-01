from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FriendlySavagesDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^shows/', include('shows.urls')),
    url(r'^shows/(?P<show_id>\d+)/$', 'shows.views.detail'),
    url(r'^admin/', include(admin.site.urls)),
)
