from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader

from shows.models import ShowListing


def home(request):
    template = loader.get_template('FriendlySavagesDjango/home.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))