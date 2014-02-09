from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from django.template.loader import render_to_string
from portal.forms import *
from django.template.context import RequestContext
from dajaxice.utils import deserialize_form
from models import *
from accounts.models import UserData
	
@dajaxice_register
def add_event(request):
	dajax = Dajax()
	form_add_event = AddEventForm()
	cont_dict = {'add_event_form':form_add_event}
	html_add_event = render_to_string('portal/add_event.html', cont_dict, RequestContext(request))
	dajax.assign('#add_event_form','innerHTML',html_add_event) 
	dajax.script('change_type()')	
	return dajax.json()
	
@dajaxice_register
def save_event(request, form):
	res = AddEventForm(deserialize_form(form))
	dajax = Dajax()
	if res is None or not res.is_valid():
		cont_dict = {'add_event_form':res}
		html_add_event = render_to_string('portal/add_event.html', cont_dict, RequestContext(request))
		dajax.assign('#add_event','innerHTML',html_add_event)
		return dajax.json()		
	nam = res.cleaned_data['name']	
	des = res.cleaned_data['description']
	dat = res.cleaned_data['date_time']
	loc = res.cleaned_data['location']
	new_event = Event(name = nam, description = des, date_time = dat, location = loc)
	new_event.save()
	success_html = '<h6>added event successfully</h6>'
	dajax.assign('#event_notif', 'innerHTML', success_html)
	dajax.script("$('#f1')[0].reset()")
	return reload_events(dajax)
	
@dajaxice_register
def delete_event(request, event_id):
	event = Event.objects.get(id = event_id)
	event.delete()
	dajax = Dajax()
	success_html = '<h6>event deleted</h6>'
	dajax.assign('#add_event', 'innerHTML', success_html)
	return reload_events(dajax)
	
@dajaxice_register
def edit_event(request, event_id):
	dajax = Dajax()
	event = Event.objects.get(id = event_id)
	form = AddEventForm(instance = event)
	cont_dict = {'edit_event_form':form, 'id' : event.id }
	html_add_event = render_to_string('portal/edit_event.html', cont_dict, RequestContext(request))
	id = '#event'+str(event_id)
	dajax.assign(id,'innerHTML',html_add_event)
	dajax.script("$('#div_events th').hide()")
	return dajax.json()
	
@dajaxice_register
def save_edited_event(request, form, event_id):
	res = AddEventForm(deserialize_form(form))
	dajax = Dajax()
	if res is None or not res.is_valid():
		cont_dict = {'edit_event_form':res}
		html_add_event = render_to_string('portal/edit_event.html', cont_dict, RequestContext(request))
		id = '#event'+str(event_id)
		dajax.assign(id,'innerHTML',html_add_event)
		return dajax.json()		
	event = Event.objects.get(id = event_id)
	event.name = res.cleaned_data['name']	
	event.description = res.cleaned_data['description']
	event.date_time = res.cleaned_data['date_time']
	event.location = res.cleaned_data['location']
	event.save()
	success_html = '<h6>event edited</h6>'
	dajax.assign('#event_notif', 'innerHTML', success_html)
	return reload_events(dajax)
	
@dajaxice_register
def add_update(request):
	dajax = Dajax()
	form_add_update = AddUpdateForm()
	cont_dict = {'add_update_form':form_add_update}
	html_add_update = render_to_string('portal/add_update.html', cont_dict, RequestContext(request))
	dajax.assign('#add_update_form','innerHTML',html_add_update)
	dajax.script('change_type()')
	return dajax.json()
	
@dajaxice_register
def save_update(request, form):
	res = AddUpdateForm(deserialize_form(form))
	dajax = Dajax()
	if res is None or not res.is_valid():
		cont_dict = {'add_update_form':res}
		html_add_update = render_to_string('portal/add_update.html', cont_dict, RequestContext(request))
		dajax.assign('#add_update_form','innerHTML',html_add_update)
		return dajax.json()		
	til = res.cleaned_data['title']
	dat = res.cleaned_data['date_time']
	upd = res.cleaned_data['update']
	new_update = Update(title = til,date_time = dat, update = upd)
	new_update.save()
	success_html = '<h6>added update successfully</h6>'
	dajax.assign('#update_notif', 'innerHTML', success_html)
	dajax.script("$('#f2')[0].reset()")
	return reload_updates(dajax)
	
@dajaxice_register
def delete_update(request, update_id):
	update = Update.objects.get(id = update_id)
	update.delete()
	dajax = Dajax()
	success_html = '<h6>update deleted</h6>'
	dajax.assign('#add_event', 'innerHTML', success_html)
	return reload_updates(dajax)
	
@dajaxice_register
def edit_update(request, update_id):
	dajax = Dajax()
	update = Update.objects.get(id = update_id)
	form = AddUpdateForm(instance = update)
	cont_dict = {'edit_update_form':form, 'id' : update.id }
	html_add_update = render_to_string('portal/edit_update.html', cont_dict, RequestContext(request))
	id = '#update'+str(update_id)
	dajax.assign(id,'innerHTML',+html_add_update)
	dajax.script("$('#div_updates th').hide()")
	return dajax.json()
	
@dajaxice_register
def save_edited_update(request, form, update_id):
	res = AddUpdateForm(deserialize_form(form))
	dajax = Dajax()
	if res is None or not res.is_valid():
		cont_dict = {'edit_update_form':res}
		html_add_update = render_to_string('portal/edit_update.html', cont_dict, RequestContext(request))
		dajax.assign('#add_event','innerHTML',html_add_update)
		return dajax.json()
	update = Update.objects.get(id = update_id)		
	update.title = res.cleaned_data['title']
	update.date_time = res.cleaned_data['date_time']
	update.update = res.cleaned_data['update']
	update.save()
	success_html = '<h6>update edited</h6>'
	dajax.assign('#add_event', 'innerHTML', success_html)
	return reload_updates(dajax)
	
@dajaxice_register
def reload(request):
	dajax = Dajax()
	events = Event.objects.all().order_by('name')
	updates = Update.objects.all().order_by('title')
	cont_dict_1 = {'events':events,'updates':updates}
	html = render_to_string('portal/div_events.html',cont_dict_1)
	dajax.assign('#div_events', 'innerHTML', html)
	html2 = render_to_string('portal/div_updates.html',cont_dict_1)
	dajax.assign('#div_updates', 'innerHTML', html2)
	return dajax.json()
	
@dajaxice_register
def reload_events(dajax):
	events = Event.objects.all().order_by('name')
	cont_dict = {'events':events}
	html = render_to_string('portal/div_events.html',cont_dict)
	dajax.assign('#div_events', 'innerHTML', html)
	return dajax.json()

@dajaxice_register
def reload_updates(dajax):
	updates = Update.objects.all().order_by('title')
	cont_dict = {'updates':updates}
	html = render_to_string('portal/div_updates.html',cont_dict)
	dajax.assign('#div_updates', 'innerHTML', html)
	return dajax.json()

@dajaxice_register
def join_event(request, user_id, event_id):
	user = UserData.objects.get(id=user_id)
	event = Event.objects.get(id=event_id)
	event.users.add(user)
	event.save()
	html2 = '<h6>Joined</h6>'
	dajax = Dajax()
	dajax.assign('#notif', 'innerHTML', html2)
	return dajax.json()