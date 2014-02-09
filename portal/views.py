from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from portal.models import *
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from portal.forms import *

@staff_member_required	
def dashboard(request):
	events = Event.objects.all()
	updates = Update.objects.all()
	form_add_event = AddEventForm()
	form_add_update = AddUpdateForm()
	rc = RequestContext(request,{'events':events, 'updates':updates,'add_event_form':form_add_event,'add_update_form':form_add_update})
	return render_to_response('portal/dashboard.html', rc)

def index(request):
	if request.user.is_staff:
		return dashboard(request)
	else:
		return HttpResponseRedirect('forum/')

@login_required		
def events(request, event_id):
	even = Event.objects.get(id = event_id)
	if request.user.is_authenticated:
		user = request.user
	rc = {'event':even, 'user':user,}
	return render_to_response('portal/event.html', rc)
	#return HttpResponse('the event name is %s' % event.name)