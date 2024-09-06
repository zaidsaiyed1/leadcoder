from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils.translation import gettext as _
from .managers import CustomUserManager
class CustomUser(AbstractUser):
   username = None
   email = models.EmailField(_('email address'),unique=True)
   is_student = models.BooleanField(default=True)
   is_quizManager = models.BooleanField(default=False)
   is_docsManager = models.BooleanField(default=False)
   is_order = models.BooleanField(default=False,blank=True)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []
   objects = CustomUserManager()

   def __str__(self):
        return self.email