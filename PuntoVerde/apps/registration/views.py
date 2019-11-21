from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms


# Create your views here.
class SignUpView(CreateView):
	form_class = UserCreationFormWithEmail
	template_name = 'registration/signup.html'


	def get_success_url(self):
		return reverse_lazy('login') + '?REGISTRADO'

	def get_form(self, form_class=None):
		form = super(SignUpView, self).get_form()
		##Personalizacion en tiempo real del form por defecto
		form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de Usuario'})
		form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Ingrese Correo'})
		form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
		form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repita Contraseña'})
		return form

	