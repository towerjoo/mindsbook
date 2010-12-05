from django.conf.urls.defaults import *
from django.conf import settings

handler500 = 'djangotoolbox.errorviews.server_error'
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #('^$', 'django.views.generic.simple.direct_to_template',
    # {'template': 'home.html'}),
    (r'^hello/$', 'guestbook.views.hello'),
    (r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:] , 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT })
        )
        
