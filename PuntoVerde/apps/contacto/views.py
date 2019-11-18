from django.shortcuts import render , redirect
from .forms import formularioContacto
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
			mensaje = request.POST.get ('mensaje', '')


			# Ok
			return redirect(reverse('contacto')+"?OK")


	return render(request,'contacto/contacto.html',{'form': formulario})

