from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from portal.models import *
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required	
def dashboard(request):
	events = Event.objects.all()
	updates = Update.objects.all()
	rc = RequestContext(request,{'events':events, 'updates':updates})
	return render_to_response('portal/dashboard.html', rc)

def index(request):

	return render_to_response('home.html', locals(), context_instance = RequestContext(request))