from django.conf.urls import patterns, url

from shows import views

urlpatterns = patterns('',
    # ex: /shows/
    url(r'^$', views.index, name='index'),
    # ex: /shows/5/
    url(r'^(?P<show_id>\d+)/$', views.detail, name='detail'),
)