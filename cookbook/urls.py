from django.conf.urls import patterns, url

from cookbook import views

urlpatterns = patterns('',
    url(r'^$', views.RecipeList.as_view(), name='recipe_list'),
    url(r'^new$', views.RecipeCreate.as_view(), name='recipe_new'),
    url(r'^(?P<pk>\d+)/$', views.RecipeDetail.as_view(), name='detail'),
    url(r'^edit/(?P<pk>\d+)$', views.RecipeUpdate.as_view(), name='recipe_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.RecipeDelete.as_view(), name='recipe_delete'),
)
