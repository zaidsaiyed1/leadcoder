import sys
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
import datetime
from .forms import *
from django.utils import timezone
from django.db.models import F, DurationField, Sum, ExpressionWrapper
from datetime import datetime, time, timedelta
import razorpay
from django.conf import settings

from django.contrib.auth import get_user_model
from django.contrib import messages
from django.forms import inlineformset_factory
user = get_user_model() 
def index(request):
 ps = Problem.objects.last()
 quiz = Quiz.objects.all()
 post = Post.objects.all().order_by('-created_at')[:3]
 return render(request,'templates/index.html',{'ps':ps,'quiz':quiz,'post':post})

def about(request):
  context = {

  }
  return render(request,'templates/about.html',context)

def documentation(request):
  post = Post.objects.all()
  context = {
'post':post,
  }
  return render(request,'templates/docs.html',context)

def contact_us(request):
  context = {

  }
  return render(request,'templates/contact.html',context)

def contactHandel(request):
  if request.method=='POST':
    namedata = request.POST['name']
    numberdata = request.POST['number']
    emaildata = request.POST['email']
    msg = request.POST['message']
    data = contactus(name=namedata,number=numberdata,email=emaildata,body=msg)
    data.save()
    messages.success(request,"Data Has Been Send Successfully!")
    return redirect('index')
def quizPlans(request):
  quizP=False
  user = request.user
  orderData = Order.objects.filter(user=user)
  orderGetData = Order.objects.filter(user=user)
  if orderData.exists():
    quizP = True
  context = {'orderData':orderData,
             'orderGetData':orderGetData,
             'quizP':quizP
             }
  return render(request,'templates/plans_for_quiz_manager.html',context)
@login_required(login_url='/login/')
def postUpload(request):
  if request.method =='POST':
     form = Postf(request.POST,request.FILES)
     if form.is_valid():
       form.save()
       return redirect('success')
  else:
     form = Postf()
   
  return render(request,'templates/post_forms.html',{'form':form})

@login_required(login_url='/login/')
def postEdit(request,pk):
  dataget = Post.objects.get(pk=pk)
  form = Postf(instance=dataget)
  if request.method =='POST':
     form = Postf(request.POST,request.FILES,instance=dataget)
     if form.is_valid():
       form.save()
       return redirect('success')
  context = {
      'form':form
  }
  return render(request,'templates/post_forms.html',context)
  
@login_required(login_url='/login/')
def postDelete(request,pk):
  post = Post.objects.get(pk=pk)
  post.delete()
  return redirect('success')

@login_required(login_url='/login/')
def conformPostForDelete(request,pk):
  data = Post.objects.get(pk=pk)
  context ={
    'data':data
  }
  return render(request,'templates/conformPost.html',context)
@login_required(login_url='/login/')
def questionUpload(request,pk):
    quizData = Quiz.objects.get(pk=pk)
    if request.method == 'POST':
      form = Questionf(request.POST,request.FILES)
      if form.is_valid():
        form.save();
        messages.success(request,"Question Has been Uploaded!")
        return redirect('controlPanelForQuizManage')
    else:
      form = Questionf()
    
    context ={
      'form':form,
      'quizData':quizData
    }
    return render(request,'templates/question_forms.html',context)
@login_required(login_url='/login/')
def questionEdit(request,pk,quid):
  quizData = Quiz.objects.get(quid = quid)
  dataget = Question.objects.get(pk=pk)
  form = Questionf(instance=dataget)
  if request.method == 'POST':
    form = Questionf(request.POST,request.FILES,instance=dataget)
    if form.is_valid():
      form.save()
      messages.success(request,"Question Has been Uploaded!")
      return redirect('controlPanelForQuizManage')
  context={
      'form':form,
      'quizData':quizData

  }
  return render(request,'templates/question_forms.html',context)
@login_required(login_url='/login/')
def deleteQuestion(request,pk):
  data = Question.objects.get(pk=pk)
  data.delete()
  messages.success(request,"Question Has been Deleted!")
  return redirect('controlPanelForQuizManage')

@login_required(login_url='/login/')
def comformQuestionForDelete(request,pk):
  data = Question.objects.get(pk=pk)
  context = {
    'data':data
  }
  return render(request,'templates/conformQuestion.html',context)

@login_required(login_url='/login/')
def answerUpload(request,pk):
 answerformset = inlineformset_factory(Question,Answer,fields=('answers','is_correct'))
 question = Question.objects.get(pk=pk)
 formset = answerformset(instance=question)
 if request.method == 'POST':
   #form=Answerf(request.POST,request.FILES)
   formset = answerformset(request.POST,instance=question)
   if formset.is_valid():
     formset.save();
     return redirect('success')
 else:
   form = answerformset()
  
 context = {
    'form':formset,
    'question':question
  }
 return render(request,'templates/answer_forms.html',context)

@login_required(login_url='/login/')
def answerEdit(request,pk):
  dataget = Answer.objects.get(pk=pk)
  form = Answerf(instance=dataget)
  if request.method == 'POST':
    form = Answerf(request.POST,request.FILES,instance=dataget)
    if form.is_valid():
      form.save();
      return redirect("success")
  
  context={
    'form':form
  }
  return render(request,'templates/answer_forms.html',context)
  
@login_required(login_url='/login/')
def conformAnswerForDelete(request,pk):
  data = Answer.objects.get(pk=pk)
  context = {
    'data':data
  }
  return render(request,'templates/conformAnswer.html',context)

@login_required(login_url='/login/')
def answerDelete(request,pk):
  data = Answer.objects.get(pk=pk)
  data.delete()
  return redirect('success')

@login_required(login_url='/login/')
def problemUpload(request):
  if request.method == 'POST':
    form = Problemf(request.POST,request.FILES)
    if form.is_valid():
     form.save();
     return redirect('success')
  else:
    form = Problemf()
  
  context = {
    'form':form
  }
  return render(request,'templates/problem_forms.html',context)

@login_required(login_url='/login/')
def problemEdit(request,pk):
  dataget = Problem.objects.get(pk=pk)
  form = Problemf(instance=dataget)
  if request.method == 'POST':
    form = Problemf(request.POST,request.FILES,instance=dataget)
    if form.is_valid():
      form.save();
      return redirect('success')
  
  context = {
    'form':form
  }
  return render(request,'templates/problem_forms.html',context)

@login_required(login_url='/login/')
def conformProblemForDelete(request,pk):
    data = Problem.objects.get(pk=pk)
    context = {
      'data':data
    }
    return render(request,'templates/conformProblem.html',context)

@login_required(login_url='/login/')
def problemDelete(request,pk):
  data = Problem.objects.get(pk=pk)
  data.delete()
  return redirect('success')

@login_required(login_url='/login/')
def answerForProblemUpload(request):
  if request.method == 'POST':
    form = AnswerForProblemf(request.POST,request.FILES)
    if form.is_valid():
     form.save();
     return redirect('success')
  else:
    form = AnswerForProblemf()
  
  context = {
    'form':form
  }
  return render(request,'templates/answer_for_problem_forms.html',context)

@login_required(login_url='/login/')
def answerForProblemEdit(request,pk):
  dataget = AnswerForProblem.objects.get(pk=pk)
  form = AnswerForProblemf(instance=dataget)
  if request.method == 'POST':
    form = AnswerForProblemf(request.POST,request.FILES,instance=dataget)
    if form.is_valid():
      form.save();
      return redirect('success')
  
  context = {
    'form':form
  }
  return render(request,'templates/answer_for_problem_forms.html',context)

@login_required(login_url='/login/')
def conformAnswerForProblemForDelete(request,pk):
    data = AnswerForProblem.objects.get(pk=pk)
    context = {
      'data':data
    }
    return render(request,'templates/conformAnswerForProblem.html',context)

@login_required(login_url='/login/')
def answerForProblemDelete(request,pk):
  data = AnswerForProblem.objects.get(pk=pk)
  data.delete()
  return redirect('success')

@login_required(login_url='/login/')
def quizUpload(request):
  userofquiz = request.user
  if request.method == 'POST':
    form =Quizf(request.POST,request.FILES)
    if form.is_valid():
     form.save();
     messages.success(request,'Quiz Has been Uploaded!')
     return redirect('controlPanelForQuizManage')
  else:
    form = Quizf()
  
  context = {
    'form':form,
    'userofquiz':userofquiz,
  }
  return render(request,'templates/quiz_forms.html',context)

@login_required(login_url='/login/')
def quizEdit(request,pk):
  userofquiz = request.user
  dataget = Quiz.objects.get(pk=pk)
  form = Quizf(instance=dataget)
  if request.method == 'POST':
    form = Quizf(request.POST,request.FILES,instance=dataget)
    if form.is_valid():
      form.save();
      messages.success(request,'Quiz Has been Edited!')
      return redirect('controlPanelForQuizManage')
  
  context = {
    'form':form,
    'userofquiz':userofquiz,
  }
  return render(request,'templates/quiz_forms.html',context)

@login_required(login_url='/login/')
def conformQuizForDelete(request,pk):
    data = Quiz.objects.get(pk=pk)
    context = {
      'data':data
    }
    return render(request,'templates/conformQuiz.html',context)

def quizDelete(request,pk):
  data = Quiz .objects.get(pk=pk)
  data.delete()
  messages.success(request,'Quiz Deleted Successfully!')
  return redirect('controlPanelForQuizManage')
  

def singlepost(request,pk):
  data = Post.objects.get(pk=pk)
  context = {
    'data':data
  }
  return render(request,'templates/single-post.html',context)

def displayAllQuiz(request):
  quiz = Quiz.objects.filter(company='@LEADCODER').all().order_by('-created_at')

  context = {
    'quiz':quiz,
  }
  return render(request,'templates/all_quiz.html',context)

@login_required(login_url='/login/')
def displayAllInvitedQuiz(request):
  quizin=False
  userdata = request.user
  quizinviteData = quizInvite.objects.filter(user=userdata)
  quizinviteGetData = quizInvite.objects.filter(user=userdata).all()
  if quizinviteData.exists():
      quizin = True
 

  context = {
    'quizin':quizin,
    'quizinviteData':quizinviteData,
    'quizinviteGetData':quizinviteGetData
  }
  return render(request,'templates/all_quiz_for_hiring.html',context)

@login_required(login_url='/login/')
def displayInstructionPageForQuiz(request,pk):
  quizTaken=False
  quizIn=False
  userdata = request.user
  quiz = Quiz.objects.get(quid=pk)
  quizSubmit = QuizSubmit.objects.filter(user=userdata,quiz=quiz)
  quizInvitedata = quizInvite.objects.filter(user=userdata,quiz=quiz)
  if quizSubmit.exists():
      quizTaken = True
  elif quizInvitedata.exists():
    quizIn = True
 

  print(quizIn)
  print(quizTaken)

  context = {
          'quiz':quiz,
          'quizTaken':quizTaken,
          'quizIn':quizIn,
      }
  return render(request,'templates/instructionPage.html',context)

def displayQuiz(request,pk):
      quizd = get_object_or_404(Quiz, pk=pk)
      start_time = timezone.now()
      end_time = start_time + timezone.timedelta(minutes=quizd.end_time)

      request.session['end_time'] = end_time.strftime('%Y-%m-%d %H:%M:%S')

      question = Question.objects.filter(quiz=pk).order_by('qid').first()
      quizd = Quiz.objects.get(pk=pk)
      answer = Answer.objects.filter(question=question).all()
      return render(request,'templates/single_quiz.html',{'questions':question,'answer':answer,'end_time':end_time})

@login_required(login_url='/login/')
def submitAnswer(request,qid,quid):
    if request.method == 'POST':
     session_end_time = request.session.get('end_time')
     end_time = datetime.strptime(session_end_time, '%Y-%m-%d %H:%M:%S')
     submitQuizUser = request.user
     if 'score' not in request.session:
        request.session['score']=0
     
     if 'Skip'in request.POST:
        if question:
             question = Question.objects.filter(quiz=quid,qid__gt=qid).exclude(qid=qid).order_by('qid').first()
             answer = Answer.objects.filter(question=question).all()
             request.session['score'] = request.session['score']  - question.marks
             final_score = request.session['score']
             print(final_score)

     question = Question.objects.filter(quiz=quid,qid__gt=qid).exclude(qid=qid).order_by('qid').first()
     answer = Answer.objects.filter(question=question).all()
     quiz = Quiz.objects.get(quid=quid)
     answersubmit = request.POST['answer_id']
     anssubmit= Answer.objects.get(id=answersubmit)
     if anssubmit.is_correct==True:
       request.session['score'] = request.session.get('score', 0) +  anssubmit.question.marks
       final_score = request.session['score']
       print(final_score) 
       if not question: 
         quizSubmitQ = QuizSubmit(quiz=quiz,score=final_score,user=submitQuizUser);
         quizSubmitQ.save();
         return quizResult(request,quid)
       else:
               return render(request, 'templates/single_quiz.html', {'questions':question, 'answer':answer,'end_time':end_time})
     else:
          print("zero") 
          if question:
               return render(request, 'templates/single_quiz.html', {'questions':question, 'answer':answer,'end_time':end_time})
          final_score = request.session['score']
          quizSubmitQ = QuizSubmit(quiz=quiz,score=final_score,user=submitQuizUser);
          quizSubmitQ.save();
          request.session.modified = True
          return quizResult(request,quid)
     
    del request.session['score']   
    return render(request, 'templates/single_quiz.html', {'questions':question, 'answer':answer,'end_time':end_time})
    
@login_required(login_url='/login/')
def quizResult(request,quid):
    del request.session['score']
    resultUser = request.user
    quiz = Quiz.objects.get(quid=quid)
    quizsub = QuizSubmit.objects.get(user=resultUser,quiz=quid)
    quizname = quiz.title
    score=quizsub.score
    context={
      'score':score,
      'quizname':quizname
        }
    return render(request,'templates/quiz_result.html',context)

@login_required(login_url='/login/')
def controlPanelForQuizManage(request):
  user = request.user
  quizUploadData = False
  quizUploadData5 = False
  quizUploadDataUni = False
  
  userorder = request.user.is_order
  if userorder == True:
    dataorder = Order.objects.get(user=user)
    basic = Plans.objects.get(name='Basic')
    medium = Plans.objects.get(name='Medium')
    advance = Plans.objects.get(name='Advance')
    if dataorder.plans==basic:
        quizCount = Quiz.objects.filter(user=user).count()
        if quizCount == 2:
           quizUploadData = True

    elif dataorder.plans==medium:
       quizCount = Quiz.objects.filter(user=user).count()
       if quizCount == 5:
           quizUploadData5 = True
    elif dataorder.plans==advance:
       quizCount = Quiz.objects.filter(user=user).count()
       quizUploadDataUni = True
     
  else:
    return redirect('success')     


  quizp = Quiz.objects.filter(user=user).all()
  # questionp = Question.objects.filter(quiz=quizp).all()
  # quizSubmited = QuizSubmit.objects.filter(quiz=quizp).all()
  context = {
     'quiz':quizp,
     'quizCount':quizCount,
     'dataorder':dataorder,
     'quizUploadData':quizUploadData,
     'quizUploadData5':quizUploadData5,
     'quizUploadDataUni':quizUploadDataUni
     
    # 'question':questionp,
    # 'quizSubmited':quizSubmited,
  }
  return render(request,'templates/admin.html',context)

@login_required(login_url='/login/')
def allQuizPageForQuizManage(request):
  userdata = request.user
  quizUploadData = False
  quizUploadData5 = False
  quizUploadDataUni = False
  
  userorder = request.user.is_order
  if userorder == True:
    dataorder = Order.objects.get(user=userdata)
    basic = Plans.objects.get(name='Basic')
    medium = Plans.objects.get(name='Medium')
    advance = Plans.objects.get(name='Advance')
    if dataorder.plans==basic:
        quizCount = Quiz.objects.filter(user=userdata).count()
        if quizCount == 2:
           quizUploadData = True

    elif dataorder.plans==medium:
       quizCount = Quiz.objects.filter(user=userdata).count()
       if quizCount == 5:
           quizUploadData5 = True
    elif dataorder.plans==advance:
       quizCount = Quiz.objects.filter(user=userdata).count()
       quizUploadDataUni = True
      
 

  quiz = Quiz.objects.filter(user=userdata).order_by('-updated_at').all()
  context = {
    'quiz':quiz,
    'quizUploadData':quizUploadData,
     'quizUploadData5':quizUploadData5,
     'quizUploadDataUni':quizUploadDataUni,
     
  }
  return render(request,'templates/allQuizPageForQuizManage.html',context)

@login_required(login_url='/login/')
def quizInvitePageForAdmin(request,pk):
  user = request.user
  quizInviteDataFor50 = False
  quizInviteDataFor70 = False
  quizInviteDataForUnlim = False 
  dataorder = Order.objects.get(user=user)
  basic = Plans.objects.get(name='Basic')
  medium = Plans.objects.get(name='Medium')
  advance = Plans.objects.get(name='Advance')
  quizData = Quiz.objects.get(pk=pk)
  quizInviteDisplay = quizInvite.objects.filter(quiz=quizData).order_by('-invited_at').all()
  quizInviteCount = quizInvite.objects.filter(quiz=quizData).count()
  if dataorder.plans == basic:
     if quizInviteCount == 50:
       quizInviteDataFor50 = True
  elif dataorder.plans == medium:
     if quizInviteCount == 70:
       quizInviteDataFor70 = True
  else:
    quizInviteDataForUnlim = True
  
       

  context = {
    'quizData':quizData,
    'quizInviteCount':quizInviteCount,
    'quizInviteDisplay':quizInviteDisplay,
    'quizInviteDataFor50':quizInviteDataFor50,
    'quizInviteDataFor70':quizInviteDataFor70,
    'quizInviteDataForUnlim':quizInviteDataForUnlim,
  }
  return render(request,'templates/quizInvitePageForAdmin.html',context)

@login_required(login_url='/login/')
def quizQuestionsPageForAdmin(request,pk):
  user = request.user
  quizQuestionDataFor20 = False
  quizQuestionDataFor40 = False
  quizQuestionDataForUnlim = False 
  dataorder = Order.objects.get(user=user)
  basic = Plans.objects.get(name='Basic')
  medium = Plans.objects.get(name='Medium')
  advance = Plans.objects.get(name='Advance')
  quizData = Quiz.objects.get(pk=pk)
  quizQuestionDisplay = Question.objects.filter(quiz=quizData).all()
  quizQuestionCount = Question.objects.filter(quiz=quizData).count()
  if dataorder.plans == basic:
     if quizQuestionCount == 20:
       quizQuestionDataFor20 = True
  elif dataorder.plans == medium:
     if quizQuestionCount == 40:
       quizQuestionDataFor40 = True
  else:
    quizQuestionDataForUnlim = True
  
       

  context = {
    'quizData':quizData,
    'quizQuestionCount':quizQuestionCount,
    'quizQuestionDisplay':quizQuestionDisplay,
    'quizQuestionDataFor20':quizQuestionDataFor20,
    'quizQuestionDataFor40':quizQuestionDataFor40,
    'quizQUestionDataForUnlim':quizQuestionDataForUnlim,
  }
  return render(request,'templates/quizQuestionPageForQuizManage.html',context)

@login_required(login_url='/login/')
def QuizSubmissionPageForQuizManage(request,quid):
  quizp = Quiz.objects.get(quid=quid)
  quizSubmited = QuizSubmit.objects.filter(quiz=quizp).all()
  context= {
     'quizSubmited':quizSubmited,
  }
  return render(request,'templates/QuizSubmissionPageForQuizManage.html',context)
def conformQuizSubmissionForDelete(request,qsid):
  quizsubmitdata = QuizSubmit.objects.get(qsid=qsid)
  context={
   'quizsubmitdata':quizsubmitdata,
  }
  return render(request,'templates/conformQuizSubmissionForDelete.html',context)

@login_required(login_url='/login/')
def quizSubmissionDelete(request,qsid):
  data = QuizSubmit.objects.get(qsid=qsid)
  data.delete()
  messages.success(request,"Quiz Submission Deleted!")
  return redirect('controlPanelForQuizManage')
  
@login_required(login_url='/login/')
def order(request,pk):
   plan = Plans.objects.get(pid=pk)
   context = {
     'plan':plan
   }
   return render(request,'templates/order.html',context)

@login_required(login_url='/login/')
def orderHandle(request,name,amount):
  if request.method == 'POST':
    cn = request.POST['cn']
    email = request.user
    plan = Plans.objects.get(name=name) 
    amountd = plan.amount
    data = Order(user=email,plans=plan,company=cn,amount=amount)
    data.save()
    amountpay = amountd*100
    print(amountpay)
  client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
  payment = client.order.create({
                         "amount":amountpay,
                         "currency": "INR",
                         "receipt": "receipt#1",
                         "line_items_total": 50000})
  data1 = Order.objects.get(user=email)
  data1.razorpay_order_id = payment['id']
  data1.one_month()
  userData = CustomUser.objects.get(email=email)
  userData.is_order = True
  userData.save()
  data1.save()
  print(payment)
  return render(
            request,
            "templates/payment.html",
            {
                "data": data,
                "payment":payment,
            },
        )
def selectLanguage(request):
  category = Category.objects.all()
  context = {
    'category':category
  }
  return render(request,'templates/select_language.html',context)

def code_Editor(request):
  selectpy = False
  selectc = False
  if request.method=='POST':
   cat = request.POST['select_id']
   category = Category.objects.get(cid=cat)
   if category.name == 'Python':
     selectpy = category
   elif category.name == 'C':
      selectc = category
   else:
     print('Nothing')
  context = {
    'selectpy':selectpy,
    'selectc':selectc,
    
  }
  return render(request,'templates/code_editor.html',context)

def contactUsRequest(request):
  if request.method == 'POST':
    name = request.POST['name']
    number = request.POST['number']
    email = request.POST['email']
    message = request.POST['message']
    data = contactus(name=name,number=number,email=email,body=message);
    data.save();
    messages.success(request,'Request Has Bean Submitted!')
  return redirect('contact')

@login_required(login_url='/login/')
def quizinvite(request,pk):
  quizData = Quiz.objects.get(pk=pk)
  if request.method == 'POST':
    form =quizInvitef(request.POST,request.FILES)
    if form.is_valid():
     form.save();
     messages.success(request,"Quiz Invite Has Been Sent!")
     return redirect('controlPanelForQuizManage')
     
  
  else:
    form = quizInvitef()
  
  context = {
    'form':form,
    'quizData':quizData,
  
  }
  return render(request,'templates/quizInviteForm.html',context)

@login_required(login_url='/login/')
def editquizinvite(request,pk,quid):
  quizData = Quiz.objects.get(quid=quid)
  dataget = quizInvite.objects.get(pk=pk)
  form = quizInvitef(instance=dataget)
  if request.method == 'POST':
    form = quizInvitef(request.POST,request.FILES,instance=dataget)
    if form.is_valid():
      form.save();
      messages.success(request,"Quiz Invite has been Edited!")
      return redirect('controlPanelForQuizManage')
  
  context = {
    'form':form,
    'quizData':quizData
  }
  return render(request,'templates/quizInviteForm.html',context)

@login_required(login_url='/login/')
def conformQuizInviteForDelete(request,pk):
    data = quizInvite.objects.get(pk=pk)
    context = {
      'data':data
    }
    return render(request,'templates/conformQuizInvite.html',context)

@login_required(login_url='/login/')
def quizInviteDelete(request,pk):
  data = quizInvite.objects.get(pk=pk)
  data.delete()
  return redirect('controlPanelForQuizManage')
  
@login_required(login_url='/login/')
def deletequizinvite(request,pk):
  dataget = quizInvite.objects.get(pk=pk)
 
  context = {
    
  }
  return render(request,'templates/quizInviteForm.html',context)

@login_required(login_url='/login/')
def allProblemStatement(request):
  submitdata = False
  userdata= request.user
  problemdata = Problem.objects.all()
  problemsubmitdata = ProblemSubmit.objects.filter(user=userdata)
  if problemsubmitdata.exists():
    submitdata = True

  context = {
      'problemdata':problemdata,
      'submitdata':submitdata,
  }
  return render(request,'templates/all_problem.html',context)

@login_required(login_url='/login/')
def problemSolvingEditior(request,proid):
  problemdata =Problem.objects.get(proid=proid)
  context={
    'problemdata':problemdata,
  }
  return render(request,'templates/problem_Statement_Editor.html',context)

@login_required(login_url='/login/')
def codeRun(request,proid):
   problemdata  = Problem.objects.get(proid=proid)
   userdata = request.user
   if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ").split(" ")
        def input():
            a = input_part[0]
            del input_part[0]
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
        codedata = ProblemSubmit(problem=problemdata,code=code_part,code_input=y,code_output = output,user=userdata)
        codedata.save();
        print(output)
   res = render(request,'templates/problem_Statement_Editor.html',{"code":code_part,"input":y,"output":output,"problemdata":problemdata})
   return res

@login_required(login_url='/login/')
def paymentSuccess(request):
  context = {}
  return render(request,'templates/successPayment.html',context)