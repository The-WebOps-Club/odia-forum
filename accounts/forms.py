

from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime

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

class DetailForm(forms.Form):
	# basic data.
	
	
	username = forms.RegexField(regex=r'^[\w.@+-]+$', max_length=30, label=_("Username"), error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})
	email = forms.EmailField(label=_("E-mail"))
	password1 = forms.CharField(widget=forms.PasswordInput, label=_("Password"))
	password2 = forms.CharField(widget=forms.PasswordInput, label=_("Password (again)"))
	group = forms.ChoiceField(label = _("Category"), choices = groups)
	
	# other details
	"""
	address = forms.CharField(label = _("Address"), max_length=200)
	institute = forms.CharField(label = _("Institute"), max_length=50)
	hostel_bool = forms.BooleanField(label= _("Hostelite?"))
	hostel = forms.CharField(max_length = 40)
	department = forms.CharField(max_length = 40)
	
	# Soft code the next line ASAP.
	batchof = forms.ChoiceField(choices = make_str(range(1955,datetime.datetime.now().year+1)), label = _("Batch of") )
	graduation_date = forms.DateField()
	course = forms.ChoiceField(choices = courses)
	"""
	
class OtherDetailsForm(forms.Form):
	 
    
	def make_str(lst):
		ret = []
		for i in lst:
			ret.append((format(i),format(i)))
		return ret
		
	address = forms.CharField(label = _("Address"), max_length=200)
	institute = forms.CharField(label = _("Institute"), max_length=50)
	hostel_bool = forms.BooleanField(label= _("Hostelite?"))
	hostel = forms.CharField(max_length = 40)
	department = forms.CharField(max_length = 40)
	
	# Soft code the next line ASAP.
	batchof = forms.ChoiceField(choices = make_str(range(1955,datetime.datetime.now().year+1)), label = _("Batch of") )
	graduation_date = forms.DateField()
	course = forms.ChoiceField(choices = courses)
	