"""Urls for the emencia Mailing List"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

from emencia import settings

urlpatterns = patterns('emencia.views.mailing_list',)

if settings.SHOW_PUBLIC_SUBSCRIPTION_PAGES:
    from emencia.forms import \
        MailingListSubscriptionForm, \
        AllMailingListSubscriptionForm

    urlpatterns += patterns(
       url(
           r'^unsubscribe/(?P<slug>[-\w]+)/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
           'view_mailinglist_unsubscribe',
           name='newsletter_mailinglist_unsubscribe'
       ),
       url(
           r'^subscribe/(?P<mailing_list_id>\d+)/',
           'view_mailinglist_subscribe',
           {
               'form_class': MailingListSubscriptionForm
           },
           name='newsletter_mailinglist_subscribe'
       ),
       url(r'^subscribe/',
           'view_mailinglist_subscribe',
           {
               'form_class': AllMailingListSubscriptionForm
           },
           name='newsletter_mailinglist_subscribe_all'
       ),
   )