from django.conf.urls import patterns, url

from shows.models import ShowListing
from core.views import generic_view

show_template_info = {
    'base_template': 'base.html',
    'active_link': '#shows',
    'template': 'shows/showlisting_list.html',
    'shows': ShowListing.shows.all()
}

urlpatterns = patterns('',
                       # ex: /shows/
                       url(r'^get_shows/$', generic_view, show_template_info),
                       url(r'^$', generic_view, show_template_info, name="get_shows"),
                       )