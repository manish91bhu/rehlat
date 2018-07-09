from django.contrib import admin
from django.urls import path,include
from user_detail.api.views import UserList

urlpatterns = [
    path('list/', UserList.as_view()),
  		
]
