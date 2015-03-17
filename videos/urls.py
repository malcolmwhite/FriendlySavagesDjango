from django.conf.urls import patterns, url

from core.views import generic_view
from models import Video

videos_template_info = {
    'base_template': 'base.html',
    'active_link': '#videos',
    'template': 'videos/index.html',
    'video_list': Video.objects.all()
}

urlpatterns = patterns('',
                       url(r'^/?$', generic_view, videos_template_info, name="get_videos"),
                       )