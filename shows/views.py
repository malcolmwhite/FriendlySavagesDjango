import urllib2
import json

from django.template import RequestContext, loader
from django.http import HttpResponse

from shows.models import ShowListing, Venue, Artist

def index(request):
    shows_list = ShowListing.objects.order_by('-date_and_time')[:5]
    template = loader.get_template('shows/index.html')
    context = RequestContext(request, {
        'shows_list': shows_list,
    })
    return HttpResponse(template.render(context))


def detail(request, show_id):
    show = ShowListing.objects.get(id=show_id)
    template = loader.get_template('shows/detail.html')
    context = RequestContext(request, {
        'show': show,
    })
    return HttpResponse(template.render(context))


def get_shows(request):
    url = 'http://api.bandsintown.com/artists/Friendly%20Savages/events.json?api_version=2.0&app_id=SOUNDLY&date=all'
    serialized_data = urllib2.urlopen(url).read()
    template = loader.get_template('shows/all_shows.html')
    packed_show_list = json.loads(serialized_data)
    unpacked_shows = [unpack_show(packed_show) for packed_show in packed_show_list]
    context = RequestContext(request, {
        'show_list': unpacked_shows
    })

    return HttpResponse(template.render(context))


def unpack_show(packed_show):
    try:
        title = packed_show[u"title"]
        datetime = packed_show[u"datetime"]
        facebook_rsvp_url = packed_show[u"facebook_rsvp_url"]
        unpacked_show = ShowListing.shows.get(title=title, datetime=datetime, facebook_rsvp_url=facebook_rsvp_url)
    except ShowListing.DoesNotExist:
        unpacked_show = ShowListing.shows.create_show(packed_show)
        unpacked_show.save()

    return unpacked_show