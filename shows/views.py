from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponse
import urllib2
import json
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

    data = json.loads(serialized_data)

    html = "<html><body><pre>Data: %s.</pre></body></html>" % json.dumps(data, indent=2)

    return HttpResponse(html)
