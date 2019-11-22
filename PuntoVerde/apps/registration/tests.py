from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
# Create your tests here.
# Prueba unitaria para comprobar el registro de usuario y su perfil

class ProfileTestCase(TestCase):
	def setUp(self):
		User.objects.create_user('userPrueba', 'correo@gmail.com', 'test4734')

	def test_profile_exists(self):
		exists = Profile.objects.filter(user__username='test').exists()
		self.assertEqual(exists, True)

