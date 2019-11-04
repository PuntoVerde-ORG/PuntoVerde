from django.db import models

# Create your models here.
class noticia(models.Model):
	titulo = models.CharField(max_length=100)
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to="contenido")
	fechacreacion = models.DateTimeField(auto_now_add=True)
	fechaupdate = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["-fechacreacion"]

	def __str__(self):
		return self.titulo



	





	