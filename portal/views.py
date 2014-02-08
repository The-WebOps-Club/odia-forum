from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from portal.models import *
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
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