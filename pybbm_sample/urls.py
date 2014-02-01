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
    url(r'^forum/', include('pybb.urls', namespace='pybb')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^dashboard/', 'portal.views.dashboard'),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),

)

urlpatterns += patterns('django.views.static', (r'^static/(?P<path>.*)$'
                        , 'serve',
                        {'document_root': settings.STATIC_ROOT,
                        'show_indexes': True}))
