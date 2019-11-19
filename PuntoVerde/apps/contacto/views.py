from django.shortcuts import render , redirect
from .forms import formularioContacto
from django.core.mail import EmailMessage
from django.urls import reverse
from django.conf import settings

# Create your views here.
def contacto(request):
	formulario = formularioContacto()


	if request.method == "POST":
		formulario = formularioContacto(data=request.POST)
		if formulario.is_valid():
			nombre = request.POST.get ('nombre', '')
			apellido = request.POST.get ('apellido', '')
			correo = request.POST.get ('correo', '')
			asunto = request.POST.get ('asunto', '')


			# # Ok
			# #Enviamos correo
			email = EmailMessage(
				"Punto Verde : Tienes un nuevo mensaje de contacto",
				"De {} {} <{}>\n\nEl mensaje es : \n\n{}".format(nombre, apellido, correo, asunto),
				"no-contestar@inbox.mailtrap.io",
				["felipe@bericul.com"],
				reply_to=[correo]




				)
			try:
				email.send()
				return redirect(reverse('contacto')+"?OK")
			except:
				return redirect(reverse('contacto')+"?FALLO")





	return render(request,'contacto/contacto.html',{'form': formulario})

