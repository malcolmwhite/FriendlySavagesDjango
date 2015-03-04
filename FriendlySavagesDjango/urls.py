from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'home.views.home', name='home'),
                       url(r'^/$', 'home.views.home', name='home'),
                       url(r'^shows/', include('shows.urls', namespace="shows")),
                       url(r'^admin/', include(admin.site.urls)),
)
