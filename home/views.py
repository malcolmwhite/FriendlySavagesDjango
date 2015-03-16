from django.template import RequestContext, loader
from django.http import HttpResponse
from core.views import generic_view


def home(request, **data):
    return apply(generic_view, (request,), data)

