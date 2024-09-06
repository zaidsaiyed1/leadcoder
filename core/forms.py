from django import forms
from .models import *

from django.forms import inlineformset_factory
class Postf(forms.ModelForm):

              class Meta:
                      model = Post
                      fields = ['title','image','body','user']

class Categoryf(forms.ModelForm):
        class Meta:
                model = Category
                fields = ['name']

class Questionf(forms.ModelForm):
        class Meta:
                model = Question
                fields = ['category','quiz','question','marks']

class Answerf(forms.ModelForm):
        class Meta:
                model = Answer
                fields = ['question','answers','is_correct']

class Problemf(forms.ModelForm):
        class Meta:
                model = Problem
                fields = ['title','body','category']

class AnswerForProblemf(forms.ModelForm):
       class Meta:
               model=AnswerForProblem
               fields = ['problems','answerforp','is_correct']


class Quizf(forms.ModelForm):
       class Meta:
               model=Quiz
               fields = ['title','category','user','company']

class Orderf(forms.ModelForm):
       class Meta:
               model=Order
               fields = ['user','plans','amount']

class quizInvitef(forms.ModelForm):
       class Meta:
               model=quizInvite
               fields = ['quiz','college','branch','passyear','phone','country','user']

