from datetime import datetime
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import *
from core.models import *
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

def registerForManager(request):
  form = UserRegisterationFormForManager()
  if request.method == 'POST':
    form = UserRegisterationFormForManager(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('email')
      messages.success(request,'Account has been created '+username)
      return redirect('login')
  else:
    form = UserRegisterationFormForManager()
  context ={
    'form':form
  }
  return render(request,'templates/registeration/registerForManager.html',context)

def loginhandle(request):
   if request.method == 'POST':
     lusername = request.POST['email']
     lpassword = request.POST['password']
     loginuser = authenticate(email=lusername,password=lpassword)
     if loginuser is not None:
        if loginuser.is_quizManager == True and loginuser.is_docsManager == False:
           if loginuser.is_order==False:
             login(request,loginuser)
             messages.success(request,'Logged In Successfully ' + lusername)
             return redirect('plansForQuiz')
           elif loginuser.is_order==True:
            data = Order.objects.get(user=loginuser)
            if data.checkUserOrderExpire():
              messages.warning(request,'Your Plans Is expired! Re-Login!')
              data.delete()
              loginuser.is_order = False
              loginuser.save()  
              return redirect('login')
            else:
              login(request,loginuser)
              messages.success(request,'Logged In Successfully ' + lusername)
              return redirect('controlPanelForQuizManage')
            
        elif loginuser.is_docsManager == True and loginuser.is_quizManager == False:
          login(request,loginuser)
          messages.success(request,'Logged In Successfuly ' + lusername)
          return redirect('controlPanelForQuizManage') 
        else:
          login(request,loginuser)
          messages.success(request,'Logged In Successfully ' + lusername)
          return redirect('index')
     else:
        messages.error(request,lusername+' Invalid Credentials!')
        return redirect('login')
     
   context ={
   
  }
   return render(request,'templates/registeration/login.html',context)

def logouthandle(request):
   logout(request)
   messages.success(request,'Logout Sucessfully')
   return redirect('index')