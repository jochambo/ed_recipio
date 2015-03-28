from django.conf.urls import patterns, url

from cookbook import views

urlpatterns = patterns('',
    # ex: /cookbook/
    url(r'^$', views.index, name='index'),
    # ex: /cookbook/5/
    url(r'^(?P<recipe_id>\d+)/$', views.detail, name='detail'),
    # ex: /cookbook/5/edit
    url(r'^(?P<recipe_id>\d+)/edit/$', views.edit, name='edit'),
)
