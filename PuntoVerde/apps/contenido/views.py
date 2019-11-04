from django.shortcuts import render
from .models import noticia

# Create your views here.
def listarnoticias(request):
    noticias = noticia.objects.all()
    return render(request, 'contenido/noticia.html', {'noticias':noticias})

# def listarnoticias(request):
# 	return render(request,'contenido/noticia.html')

