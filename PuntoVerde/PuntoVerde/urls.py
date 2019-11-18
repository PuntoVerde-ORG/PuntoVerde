"""PuntoVerde URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.contenido import views as contenido_views
from apps.inicio import views as inicio_views
from apps.contacto import views as contacto_views

# ver imagenes 
from django.conf import settings

urlpatterns = [
    path('', inicio_views.inicio, name='index'),
    path('Contáctanos', contacto_views.contacto, name='contacto'),
    path('QuienesSomos', inicio_views.somos, name='somos'),
    path('noticias', contenido_views.listarnoticias, name='listarnoticias'),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)