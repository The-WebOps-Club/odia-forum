from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybbm_sample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^forum/',include('pybbm_tag.urls', namespace='pybb_tag')),
    url(r'^forum/', include('pybb.urls', namespace='pybb')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^dashboard/', 'portal.views.dashboard'),
	url(r'^home/(?P<insti>[a-z]+)/dashboard', 'portal.views.homepage_admin'),
	url(r'^home/(?P<insti>[a-z]+)/', 'portal.views.homepage'),	
    url(r'^$', 'portal.views.index'),
	url(r'^events/(?P<event_id>\d+)/','portal.views.events'),
    url(r'^dajaxice/',include('dajaxice.urls')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

)

urlpatterns += patterns('django.views.static', (r'^static/(?P<path>.*)$'
                        , 'serve',
                        {'document_root': settings.STATIC_ROOT,
                        'show_indexes': True}))
