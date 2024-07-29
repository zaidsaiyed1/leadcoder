from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.http import HttpResponse
# Create your views here.
def testing(request):
              return HttpResponse('Sucessfully Temp')

def register(request):
  form = UserRegisterationForm()
  if request.method == 'POST':
    form = UserRegisterationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('email')
      messages.success(request,'Account has been created '+username)
      return redirect('login')
  else:
    form = UserRegisterationForm()
  context ={
    'form':form
  }
  return render(request,'templates/registeration/register.html',context)


def loginhandle(request):
   if request.method == 'POST':
     lusername = request.POST['email']
     lpassword = request.POST['password']
     loginuser = authenticate(email=lusername,password=lpassword)
     if loginuser is not None:
        login(request,loginuser)
        messages.success(request,'Logged In SuccessFuly ' + lusername)
        return redirect('index')


   context ={
   
  }
   return render(request,'templates/registeration/login.html',context)
