from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *
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
  context = {

  }
  return render(request,'templates/docs.html',context)

def contact_us(request):
  context = {

  }
  return render(request,'templates/contact.html',context)


def postUpload(request):
  if request.method =='POST':
     form = Postf(request.POST,request.FILES)
     if form.is_valid():
       form.save()
       return redirect('success')
  else:
     form = Postf()
   
  return render(request,'templates/post_forms.html',{'form':form})


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
  

def postDelete(request,pk):
  post = Post.objects.get(pk=pk)
  post.delete()
  return redirect('success')

def conformPostForDelete(request,pk):
  data = Post.objects.get(pk=pk)
  context ={
    'data':data
  }
  return render(request,'templates/conformPost.html',context)

def questionUpload(request):
    if request.method == 'POST':
      form = Questionf(request.POST,request.FILES)
      if form.is_valid():
        form.save();
        return redirect('success')
    else:
      form = Questionf()
    
    context ={
      'form':form
    }
    return render(request,'templates/question_forms.html',context)

def questionEdit(request,pk):
  dataget = Question.objects.get(pk=pk)
  form = Questionf(instance=dataget)
  if request.method == 'POST':
    form = Questionf(request.POST,request.FILES,instance=dataget)
    if form.is_valid():
      form.save()
      return redirect('success')
   
  context={
      'form':form
  }
  return render(request,'templates/question_forms.html',context)

def deleteQuestion(request,pk):
  data = Question.objects.get(pk=pk)
  data.delete()
  return redirect('success')

def comformQuestionForDelete(request,pk):
  data = Question.objects.get(pk=pk)
  context = {
    'data':data
  }
  return render(request,'templates/conformQuestion.html',context)

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
  

def conformAnswerForDelete(request,pk):
  data = Answer.objects.get(pk=pk)
  context = {
    'data':data
  }
  return render(request,'templates/conformAnswer.html',context)

def answerDelete(request,pk):
  data = Answer.objects.get(pk=pk)
  data.delete()
  return redirect('success')

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

def conformProblemForDelete(request,pk):
    data = Problem.objects.get(pk=pk)
    context = {
      'data':data
    }
    return render(request,'templates/conformProblem.html',context)

def problemDelete(request,pk):
  data = Problem.objects.get(pk=pk)
  data.delete()
  return redirect('success')

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

def conformAnswerForProblemForDelete(request,pk):
    data = AnswerForProblem.objects.get(pk=pk)
    context = {
      'data':data
    }
    return render(request,'templates/conformAnswerForProblem.html',context)

def answerForProblemDelete(request,pk):
  data = AnswerForProblem.objects.get(pk=pk)
  data.delete()
  return redirect('success')


def quizUpload(request):
  if request.method == 'POST':
    form =Quizf(request.POST,request.FILES)
    if form.is_valid():
     form.save();
     return redirect('success')
  else:
    form = Quizf()
  
  context = {
    'form':form
  }
  return render(request,'templates/quiz_forms.html',context)

def quizEdit(request,pk):
  dataget = Quiz.objects.get(pk=pk)
  form = Quizf(instance=dataget)
  if request.method == 'POST':
    form = Quizf(request.POST,request.FILES,instance=dataget)
    if form.is_valid():
      form.save();
      return redirect('success')
  
  context = {
    'form':form
  }
  return render(request,'templates/quiz_forms.html',context)

def conformQuizForDelete(request,pk):
    data = Quiz.objects.get(pk=pk)
    context = {
      'data':data
    }
    return render(request,'templates/conformQuiz.html',context)

def quizDelete(request,pk):
  data = Quiz .objects.get(pk=pk)
  data.delete()
  return redirect('success')
  

def singlepost(request,pk):
  data = Post.objects.get(pk=pk)
  context = {
    'data':data
  }
  return render(request,'templates/single-post.html',context)

def displayAllQuiz(request):
  quiz = Quiz.objects.all()
 
  context = {
    'quiz':quiz
  }
  return render(request,'templates/all_quiz.html',context)

def diplayQuiz(request,pk):
      question = Question.objects.filter(quiz=pk).order_by('qid').first()
      answer = Answer.objects.filter(question=question).all()
      return render(request,'templates/single_quiz.html',{'questions':question,'answer':answer})

def submitAnswer(request,qid,quid):
    if request.method == 'POST':
     if 'Skip'in request.POST:
        if question:
             question = Question.objects.filter(quiz=quid,qid__gt=qid).exclude(qid=qid).order_by('qid').first()
             answer = Answer.objects.filter(question=question).all()
             request.session['score'] = request.session['score']  - question.marks
             final_score = request.session['score'] 

     submitQuizUser = request.user
     if 'score' not in request.session:
        request.session['score']=0

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
               return render(request, 'templates/single_quiz.html', {'questions':question, 'answer':answer})
     else:
          if question:
               return render(request, 'templates/single_quiz.html', {'questions':question, 'answer':answer})
          final_score = request.session['score'] 
          quizSubmitQ = QuizSubmit(quiz=quiz,score=final_score,user=submitQuizUser);
          quizSubmitQ.save();
          
          request.session.modified = True
          return quizResult(request,quid)
     
    del request.session['score']   
    return render(request, 'templates/single_quiz.html', {'questions':question, 'answer':answer})
    
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

def controlPanelForQuizManage(request):
  # quizp = Quiz.objects.all()
  # questionp = Question.objects.filter(quiz=quizp).all()
  # quizSubmited = QuizSubmit.objects.filter(quiz=quizp).all()
  context = {
  #  'quiz':quizp,
  #  'question':questionp,
  #  'quizSubmited':quizSubmited,
  }
  return render(request,'templates/admin.html',context)

def allQuizPageForQuizManage(request):
  quiz = Quiz.objects.all()
  context = {
    'quiz':quiz
  }
  return render(request,'templates/allQuizPageForQuizManage.html',context)

def QuizSubmissionPageForQuizManage(request):
  quizp = Quiz.objects.get(quid=4)
  quizSubmited = QuizSubmit.objects.filter(quiz=quizp).all()
  context= {
     'quizSubmited':quizSubmited,
  }
  return render(request,'templates/QuizSubmissionPageForQuizManage.html',context)

def QuizResultPageForQuizManage(request):
  context = {

  }
  return render(request,'templates/QuizResultPageForQuizManage.html',context)

def success(request):
  return HttpResponse('Upload SuccessFully')

def code_Editor(request):
  return render(request,'templates/pycode_editor.html',{})