from django.conf.urls import patterns, url

from cookbook import views

urlpatterns = patterns('',
    # ex: /cookbook/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /cookbook/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /cookbook/5/edit
    url(r'^(?P<recipe_id>\d+)/edit/$', views.edit, name='edit'),
)
