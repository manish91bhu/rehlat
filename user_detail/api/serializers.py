from django.contrib.auth.models import User
from user_detail.models import UserProfile
from rest_framework import serializers

class UserSerilizer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields =('id', 'is_superuser', 'username', 'is_active', 'first_name')

class UserDetailSerilizer(serializers.ModelSerializer):
	user = UserSerilizer()
	class Meta:	
		model = UserProfile
		#fields = '__all__'
		fields = ('user', 'designation', 'salary','department', 'phone','dob')
