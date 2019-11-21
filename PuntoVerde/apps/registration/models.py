from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class perfiles(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='perfiles', null=True, blank=True)
	nick = models.TextField (null=True , blank=True)
	descripcion = models.TextField (null=True , blank=True)
	link = models.URLField(max_length=250, null=True , blank=True)
