from django.contrib import admin
from .models import noticia
# Register your models here.

class NewAdmin(admin.ModelAdmin):
    readonly_fields = ('fechacreacion', 'fechaupdate')

admin.site.register(noticia,NewAdmin)