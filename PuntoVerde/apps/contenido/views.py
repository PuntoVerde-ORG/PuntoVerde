from django.shortcuts import render
from .models import noticia
# Create your views here.
def noticia(resquest):
	noticias = noticia.objects.all()
	return render(resquest,'contenido/noticia.html', {'noticias':noticias})

