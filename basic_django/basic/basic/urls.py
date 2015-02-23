from django.conf.urls import patterns, include, url
from django.contrib import admin
from app_test.views import home

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
