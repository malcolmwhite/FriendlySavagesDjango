from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse


def home(request):
    template = loader.get_template('home/index.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))
