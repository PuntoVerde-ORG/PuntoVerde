from django import forms

class formularioContacto(forms.Form):
	nombre = forms.CharField(label="nombre", max_length=30, min_length=4, required=True, widget=forms.TextInput(
		attrs={'class':'form-control','id':'validationDefault01'}
		))
	apellido = forms.CharField(label="apellido",  max_length=30, min_length=4, required=True, widget=forms.TextInput(
		attrs={'class':'form-control','id':'validationDefault02'}
		))
	correo = forms.EmailField(label="correo", required=True, widget=forms.EmailInput(
		attrs={'class':'form-control','id':'validationDefault03'}
		))
	correo2 = forms.EmailField(label="correo2", required=True, widget=forms.EmailInput(
		attrs={'class':'form-control','id':'validationDefault04'}
		))
	asunto = forms.CharField(label="asunto", max_length=250, min_length=10,required=True, widget=forms.Textarea(
		attrs={'class':'form-control','id':'validationDefault04'}
		))
	