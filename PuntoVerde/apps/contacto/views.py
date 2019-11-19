from django.shortcuts import render , redirect
from .forms import formularioContacto
from django.core.mail import send_mail , EmailMessage
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

			#Creamos el correo 
			subject = 'Gracias por enviarnos tus consultas'
			message = "Hemos recibido tu formulario ,muy pronto nos pondremos en cóntacto contigo <{} {}>\n\nTu mensaje es : \n\n{}".format(nombre, apellido, asunto)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [correo]


			# # # Ok
			# # #Enviamos correo
			email = EmailMessage(
				"Punto Verde : Tienes un nuevo mensaje de contacto",
				"De {} {} <{}>\n\nEl mensaje es : \n\n{}".format(nombre, apellido, correo, asunto),
				"no-contestar@gmail.com",
				["contacto.punto.verde2019@gmail.com"],
				reply_to=[correo]




			)

			try:
				email.send()
				send_mail( subject, message, email_from, recipient_list )
				return redirect(reverse('contacto')+"?OK")
			except:
				return redirect(reverse('contacto')+"?FALLO")





	return render(request,'contacto/contacto.html',{'form': formulario})

