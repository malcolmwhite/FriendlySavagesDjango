from django.template import RequestContext, loader
from django.http import HttpResponse
import urllib2
import json
from shows.serializers import ShowListingSerializer
from shows.models import ShowListing


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
    url = 'http://api.bandsintown.com/artists/Friendly%20Savages/events?format=json&app_id=SOUNDLY&date=all'
    serialized_data = urllib2.urlopen(url).read()
    template = loader.get_template('shows/all_shows.html')
    show_list = json.loads(serialized_data)
    serializer = ShowListingSerializer(show_list)
    context = RequestContext(request, {
        'show_list': serializer
    })

    return HttpResponse(template.render(context))
