from django.template import RequestContext, loader
from django.http import HttpResponse

from models import Video


def index(request):
    video_list = Video.objects.all()
    template = loader.get_template('videos/index.html')
    context = RequestContext(request, {
        'video_list': video_list,
    })
    return HttpResponse(template.render(context))