from django.template import RequestContext, loader
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.utils import timezone
from shows.models import ShowListing


def detail(request, show_id):
    show = ShowListing.shows.get(id=show_id)
    template = loader.get_template('shows/detail.html')
    context = RequestContext(request, {
        'show': show,
    })
    return HttpResponse(template.render(context))


def all_shows(request):
    shows = ShowListing.shows.all()
    template = loader.get_template('shows/showlisting_list.html')
    context = RequestContext(request, {
        'shows': shows,
    })
    return HttpResponse(template.render(context))

