from django import forms

class formularioContacto(forms.Form):
	nombre = forms.CharField(label="Nombres", required=True, widget=forms.TextInput(
		attrs={'class':'form-control','id':'validationDefault01'}
		))
	apellido = forms.CharField(label="Apellido", required=True, widget=forms.TextInput(
		attrs={'class':'form-control','id':'validationDefault02'}
		))
	correo = forms.EmailField(label="Correo", required=True, widget=forms.EmailInput(
		attrs={'class':'form-control','id':'validationDefault03'}
		))
	correo2 = forms.EmailField(label="Confirmar Correo", required=True, widget=forms.EmailInput(
		attrs={'class':'form-control','id':'validationDefault04'}
		))
	asunto = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(
		attrs={'class':'form-control','id':'validationDefault04'}
		))
	