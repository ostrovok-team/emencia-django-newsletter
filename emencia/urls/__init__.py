"""Default urls for the emencia"""
try:
    from django.conf.urls.defaults import url
    from django.conf.urls.defaults import include
    from django.conf.urls.defaults import patterns
except ImportError:
    # Django 1.6+
    from django.conf.urls import url, include, patterns


urlpatterns = patterns('',
                       url(r'^mailing/', include('emencia.urls.mailing_list')),
                       url(r'^tracking/', include('emencia.urls.tracking')),
                       url(r'^statistics/', include('emencia.urls.statistics')),
                       url(r'^', include('emencia.urls.newsletter')),
                       )
