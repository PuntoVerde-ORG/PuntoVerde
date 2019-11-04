from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def inicio(resquest):
	return render(resquest,'inicio/index.html')


def somos(resquest):
	return render(resquest,'inicio/somos.html')


def contacto(resquest):
	return render(resquest,'inicio/contacto.html')



# def registro(resquest):
# 	return render(resquest,'inicio/somos.html')