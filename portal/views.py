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

def events(request, event_id):
	even = Event.objects.get(id = event_id)
	all_users = even.users.all()
	if request.user.is_authenticated():
		user = request.user	
		data = UserData.objects.get(user = user)
		if data in even.users.all():
			joined = 1
		else:
			joined = 0
		num = len(all_users) - joined	
		rc = {'event':even, 'user':user, 'joined':joined, 'num':num}
	else:
		num = len(all_users)
		joined = 0
		rc = {'event':even, 'joined':joined, 'num':num,}
	return render_to_response('portal/event.html', rc)

def homepage(request, insti):
	insti = insti.capitalize()
	homepage = Homepage.objects.get(institute = insti)
	cont = {'homepage':homepage}
	return render_to_response('portal/homepage.html', cont)
	
def homepage_admin(request, insti):
	if request.user.username != insti+'_admin' and not request.user.is_superuser:
		return HttpResponseRedirect('/home/'+insti)
	insti = insti.capitalize()
	homepage = Homepage.objects.get(institute = insti)
	cont = {'homepage':homepage}
	return render_to_response('portal/homepage_admin.html',cont)