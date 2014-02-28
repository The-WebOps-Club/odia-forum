from django.shortcuts import render
from pybb.models import *
from pybbm_tag.models import Tag
from pybb.views import ForumView,AddPostView,EditPostView,TopicView


def add_tag(request,**kwargs):	
	# check permissions before calling this function
	# in kwargs we expect the LABEL of the tag to add(not object) and the TOPIC object(not name).
	topic = kwargs['topic']
	tagname = kwargs['tag']
	
	lst = Tag.objects.filter(label = tagname)
	if not lst.count() == 0:
		lst[0].topics.add(topic)
		lst[0].save()
	else:
		tag = Tag(label = tagname,desc="Empty")
		tag.save()
		tag.topics.add(topic)
		
def remove_all_tags(request,**kwargs):
	topic = kwargs['topic']
	for i in Tag.objects.filter(topics__in = [topic]):
		i.topics.remove(topic)
	
def remove_tag(request,**kwargs):
	# check permissions before calling this function.
	topic = kwargs['topic']
	tagname = kwargs['tag']
	
	lst = Tag.objects.filter(label = tagname)
	lst[0].topics.remove(topic)

	
# tag additions to the views that are affected by tags.
class AddPostViewWrapper(AddPostView):
	def post(self, request, *args, **kwargs):
		try:
			ret = super(AddPostViewWrapper, self).post(request, *args, **kwargs)
			taglist = request.POST['taglist'].split('+')
		#import pdb;pdb.set_trace()
			for i in taglist:
				add_tag(request, topic=self.object.topic, tag=i)
		except KeyError:
			pass
		return ret
	
	def get_context_data(self,**kwargs):
		ctx = super(AddPostViewWrapper, self).get_context_data(**kwargs)
		if ctx['forum']:
			ctx['taglist_input'] = 1
			
		return ctx


class ForumViewWrapper(ForumView):
	def get_context_data(self):
		ctx = super(ForumViewWrapper, self).get_context_data()
		topic_list = ctx['topic_list']
		tags = []
		for i in topic_list:
			tags.append(Tag.objects.filter(topics__in = [i]))
		ctx['tags'] = Tag.objects.all()
		return ctx

class TopicViewWrapper(TopicView):
		def get_context_data(self):
			ctx = super(TopicViewWrapper, self).get_context_data()
			ctx['tags'] = Tag.objects.all()
			return ctx
		
class EditPostViewWrapper(EditPostView):
	def post(self, request, *args, **kwargs):
		ret = super(EditPostViewWrapper, self).post(request, *args, **kwargs)
		try:
			taglist = request.POST['taglist'].split('+')
			remove_all_tags(request, topic=self.object.topic)
			for i in taglist:
				add_tag(request, topic=self.object.topic, tag=i)
		except KeyError:
			pass
		return ret
	def make_tag_string(self,topic):	
		str = ""
		for i in Tag.objects.filter(topics__in = [topic]):
			str+=(i.label+"+")
		if len(str) > 0:
			str = str[:-1]
		return str
	def get_context_data(self, **kwargs):
		ctx = super(EditPostViewWrapper, self).get_context_data(**kwargs)
		post = ctx['post']
		if post.topic.user == self.request.user:
			ctx['taglist_input'] = 1
			ctx['taglist_initial'] = self.make_tag_string(post.topic)
		return ctx