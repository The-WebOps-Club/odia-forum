

from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from django.contrib.auth.models import User
from accounts.models import UserData
groups = (
('1','Current Student/Faculty'),
('2','Verified Alumni'),
('3','Alumni'),
('4','General')
)

courses = (
('B.Tech','B.Tech'),
('M.Tech','M.Tech'),
('M.S.','M.S.'),
('M.A.','M.A.'),
('M.B.A.','M.B.A.')
)


mail_hosts = ['smail.iitm.ac.in']
class DetailForm(forms.Form):
	# basic data.
	
	
	username = forms.RegexField(regex=r'^[\w.@+-]+$', max_length=30, label=_("Username"), error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})
	first_name = forms.RegexField(regex=r'^[\w.@+-]+$', max_length=50, label=_("First Name"), error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})
	last_name = forms.RegexField(regex=r'^[\w.@+-]+$', max_length=50, label=_("Last Name"), error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})
	email = forms.EmailField(label=_("E-mail"))
	password1 = forms.CharField(widget=forms.PasswordInput, label=_("Password"))
	password2 = forms.CharField(widget=forms.PasswordInput, label=_("Password (again)"))
	group = forms.ChoiceField(label = _("Category"), choices = groups, required = 'true')

	def __init__(self,*args,**kwargs):
		super(DetailForm, self).__init__(*args,**kwargs)
		self.fields['email'].widget.attrs['class'] = 'form-control'	# for some reason email-field doesn't automatically set it's class to form-control.

	def clean_username(self):
		if(User.objects.filter(username=self.cleaned_data['username']).count() != 0):
			raise forms.ValidationError(_("Duplicate User IDs"))
		return self.cleaned_data['username']
		
	def clean(self):
		if((User.objects.filter(email=self.cleaned_data['email']).count() != 0 ) or (UserData.objects.filter(email=self.cleaned_data['email']).count() !=0 )):
			raise forms.ValidationError(_("Duplicate Email IDs"))
		
		mail_host = self.cleaned_data['email'].split("@")[1]
		if(mail_host.lower() not in mail_hosts and (self.cleaned_data['group'] == "1")):
			raise forms.ValidationError(_("Current Students/Faculty please register with your institute email ID."))
	
		return self.cleaned_data
	# other details

class AccountEditForm(forms.ModelForm):
	first_name = forms.CharField(label=_("First Name"),max_length = 30)
	last_name = forms.CharField(label=_("Last Name"),max_length = 30)
	email = forms.EmailField(label = _("Email"))
	class Meta:
		model = UserData
		fields = ['first_name','email','last_name','address', 'institute', 'hostel_bool', 'hostel','department','batchof','course']
		
	def save(self, *args, **kwargs):
		obj = super(Beta,self).save(*args,**kwargs)
		obj.user.first_name = self.cleaned_data["first_name"]
		obj.user.last_name = self.cleaned_data["last_name"]
		obj.email = obj.user.email;
		obj.user.email = self.cleaned_data['email']
		obj.user.save()
		return obj
