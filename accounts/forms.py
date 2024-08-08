from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
class UserRegisterationForm(UserCreationForm):
        email = forms.EmailField()
        class Meta:
                model=CustomUser
                fields = ('first_name','last_name','email','password1','password2')

class UserRegisterationFormForManager(UserCreationForm):
        email = forms.EmailField()
        class Meta:
                model=CustomUser
                fields = ('email','password1','password2','is_quizManager','is_docsManager')
