from django.urls import path
from . import views

urlpatterns = [
   path('user/',views.testing,name='user'),
   path('register/',views.register,name='register'),
   path('registerForManager/',views.registerForManager,name='registerForManager'),
   path('login/',views.loginhandle,name='login'),
   path('logout/',views.logouthandle,name='logout'),
]