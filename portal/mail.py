from accounts.models import UserData
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from pybbm_sample.settings import DEFAULT_FROM_EMAIL

# Takes two arrays as arguments. Plain strings except 'all' WILL NOT work
def make_list(category, iit):
	list = []
	
	if category == 'all':
		if iit == 'all':
			user_list = UserData.objects.all()
			for user in user_list:	
				list.append(str(user.user.email))
		else:
			user_list = UserData.objects.filter(institute__in = iit)
			for user in user_list:	
				list.append(str(user.user.email))
			
	elif iit == 'all':
		group_list = Group.objects.filter(name__in = category)
		user_list = []
		for group in group_list:
			user_list.extend(group.user_set.all())
		for user in user_list:	
			list.append(str(user.email))
		
	else:
		group_list = Group.objects.filter(name__in = category)
		user_list = []
		for group in group_list:
			user_list.extend(group.user_set.filter(userdata__institute__in = iit))
		for user in user_list:	
			list.append(str(user.email))
	
	return list

def mail(subj, msg, category, iit):
	list = make_list(category, iit)
	send_mail(subject = subj, message = msg, recipient_list = list, from_email = DEFAULT_FROM_EMAIL)
