from django.shortcuts import render
from django.views.generic.edit import UpdateView


from registration.backends.default.views import RegistrationView,ActivationView
from accounts.forms import DetailForm,AccountEditForm
from accounts.models import UserData
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse



permission_lists = {'test':['pybb.add_post','pybb.view_post']}

class AccountRegistrationView(RegistrationView):
	form_class = DetailForm
	def register(self, request, **cleaned_data):
		
		user = super(AccountRegistrationView, self).register(request, **cleaned_data)
		user.groups.add(cleaned_data['group'])
		user_profile = UserData(user = user,email = user.email)
		user_profile.save()
		return user

class AccountEditView(UpdateView):

	form_class = AccountEditForm
	template_name = "registration/registration-form.html"
	
	def dispatch(self, request, *args, **kwargs):
	
		if not self.request.user.is_authenticated:
			return redirect("accounts:login")
		else:
			return super(UpdateView, self).dispatch(request,*args,**kwargs);
	
	def get_object(self, queryset=None):
		return UserData.objects.filter(user=self.request.user)[0]
	
	def get_success_url(self):
		return reverse("pybb:edit_profile")
	
	def get_context_data(self,**kwargs):
		ctx = super(AccountEditView, self).get_context_data(**kwargs)
		ctx["form"] = self.form_class(instance = UserData.objects.filter(user=self.request.user)[0],initial={"first_name":self.request.user.first_name,"last_name":self.request.user.last_name,"email":self.request.user.email})
		return ctx
		
	pass;