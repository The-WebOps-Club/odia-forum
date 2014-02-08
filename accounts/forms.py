

from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from django.contrib.auth.models import User

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
	
	def clean_username(self):
		if(User.objects.filter(username=self.cleaned_data['username']).count() != 0):
			raise forms.ValidationError(_("Duplicate User IDs"))
		return self.cleaned_data['username']
		
	def clean(self):
		if(User.objects.filter(email=self.cleaned_data['email']).count() != 0):
			raise forms.ValidationError(_("Duplicate Email IDs"))
		
		mail_host = self.cleaned_data['email'].split("@")[1]
		if(mail_host.lower() not in mail_hosts and (self.cleaned_data['group'] == "1")):
			raise forms.ValidationError(_("Current Students/Faculty please register with your institute email ID."))
	
		return self.cleaned_data
	# other details
	
