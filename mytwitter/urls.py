from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytwitter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'feed.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/([-\w]+)/$', 'feed.views.user_post', name='user_post'),
    url(r'^add/$', 'feed.views.add_post', name='add_post')
)
