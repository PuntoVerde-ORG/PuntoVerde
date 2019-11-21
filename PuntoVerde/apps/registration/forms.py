from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
	email = forms.EmailField(required=True, help_text="Ingrese un correo Valido")

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("El email ya esta en uso, intente nuevamente.")
		return email
