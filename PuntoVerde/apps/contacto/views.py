from django.shortcuts import render , redirect
from .forms import formularioContacto
from django.core.mail import EmailMessage
from django.urls import reverse

# Create your views here.
def contacto(request):
	formulario = formularioContacto()


	if request.method == "POST":
		formulario = formularioContacto(data=request.POST)
		if formulario.is_valid():
			nombre = request.POST.get ('nombre', '')
			apellido = request.POST.get ('apellido', '')
			correo = request.POST.get ('correo', '')
			correo2 = request.POST.get ('correo2', '')
			asunto = request.POST.get ('asunto', '')


			# Ok
			#Enviamos correo
			correo= EmailMessage (
				"Punto Verde : Hemos Recibido su formulario",
				"De {} <{}>\n\nTu Mensaje:\n\n{}".format(nombre,apellido,correo,asunto),
				"felipeandrescatalan.18@gmail.com",
				["transmutadordef@gmail.com"],
				reply_to=[correo]
			)

			try:
				email.send()
				return redirect(reverse('contacto')+"?OK")
			except:
				#Algo salio mal 
				return redirect(reverse('contacto')+"?FALLO")

			


	return render(request,'contacto/contacto.html',{'form': formulario})

