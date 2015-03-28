from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^cookbook/', include('cookbook.urls', namespace="cookbook")),
    url(r'^admin/', include(admin.site.urls)),
)
