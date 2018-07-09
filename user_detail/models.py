from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)

	designation = models.CharField(max_length=100, null=True, blank=True)
	department = models.CharField(max_length=100, null=True, blank=True)
	salary = models.FloatField(null=False, blank=False)
	phone = models.CharField(max_length=15, null=False, blank=False)
	dob = models.DateField(null=False, blank=False)

	def __str__(self):
		return self.user.username
