
from .serializers import UserDetailSerilizer
from user_detail.models import UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, \
    SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny


class UserList(generics.ListCreateAPIView):
	
	authentication_classes = (TokenAuthentication,SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	serializer_class = UserDetailSerilizer

	def get_queryset(self):
		# for admin user
		if self.request.user.is_superuser:
			queryset = UserProfile.objects.all()
		else:
			# for normal user
			queryset = UserProfile.objects.filter(user=self.request.user.id)

		return queryset

