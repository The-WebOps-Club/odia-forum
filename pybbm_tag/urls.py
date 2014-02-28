
from django.conf.urls import patterns, include, url
from pybbm_tag.views import AddPostViewWrapper,ForumViewWrapper, EditPostViewWrapper, TopicViewWrapper

urlpatterns = patterns('',
							url('^forum/(?P<forum_id>\d+)/topic/add/$', AddPostViewWrapper.as_view(), name='add_topic'),
							url('^forum/(?P<pk>\d+)/$', ForumViewWrapper.as_view(), name='forum'),
							url('^post/(?P<pk>\d+)/edit/$', EditPostViewWrapper.as_view(), name='edit_post'),
							url('^topic/(?P<pk>\d+)/$', TopicViewWrapper.as_view(), name='topic'),
                       )