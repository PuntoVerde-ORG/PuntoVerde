from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def inicio(request):
	return render(request,'inicio/index.html')


def somos(request):
	return render(request,'inicio/somos.html')


def contacto(request):
	return render(request,'inicio/contacto.html')



# def registro(resquest):
# 	return render(resquest,'inicio/somos.html')