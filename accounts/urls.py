from django.urls import path
from . import views

urlpatterns = [
   path('user/',views.testing,name='user'),
   path('register/',views.register,name='register'),
   path('login/',views.loginhandle,name='login'),
]