from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    (r'^auth/', include('rest_framework_social_oauth2.urls')),
    url('', include('social.apps.django_app.urls', namespace='social'))
)
