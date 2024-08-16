import random
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from autoslug import AutoSlugField
from accounts.models import CustomUser
from django.conf import settings

class Post(models.Model):
       pid = models.BigAutoField(primary_key=True)
       title = models.CharField(max_length=200,null=False)
       image = models.ImageField(upload_to='images/')
       slug = AutoSlugField(populate_from='title',unique=True,null=True)
       body = RichTextUploadingField()
       user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
       def __str__(self):
              return self.title

class Meta: 
       db_table = "Post_table"


class Category(models.Model):
       cid = models.BigAutoField(primary_key=True)
       name = models.CharField(max_length=300,null=False)
       def __str__(self):
              return self.name

class Quiz(models.Model):
       quid = models.BigAutoField(primary_key=True)
       title = models.CharField(max_length=200,null=True)
       category = models.ForeignKey(Category,on_delete= models.CASCADE)
       user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
       def __str__(self):
              return self.title       

class Question(models.Model):
       qid = models.BigAutoField(primary_key=True)
       category = models.ForeignKey(Category,on_delete= models.CASCADE) 
       quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
       question = RichTextUploadingField()
       marks = models.IntegerField()
       def __str__(self):
              return self.question
       def get_answer(self):
              answers = list(Answer.objects.filter(question=self))
              data = []
              random.shuffle(answers)
               
              for  answers in answers:
                  data.append({
                'answers' :answers.answers, 
                'is_correct':answers.is_correct
              })
              return data


class Answer(models.Model):
       question = models.ForeignKey(Question,on_delete= models.CASCADE)
       answers = models.CharField(max_length=200)
       is_correct = models.BooleanField(default=False)
       def __str__(self):
              return self.answers
 
class Problem(models.Model):
       proid = models.BigAutoField(primary_key=True)
       title = models.CharField(max_length=800,null=False)
       slug = AutoSlugField(populate_from='title',unique=True,null=True)
       body = RichTextUploadingField()
       category = models.ForeignKey(Category,on_delete= models.CASCADE,null=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
       def __str__(self):
              return self.title

class AnswerForProblem(models.Model):
       problems = models.ForeignKey(Problem,on_delete= models.CASCADE)
       answerforp = RichTextUploadingField()
       is_correct = models.BooleanField(default=False)
       def __str__(self):
              return self.answerforp

class QuizSubmit(models.Model):
       qsid = models.BigAutoField(primary_key=True)
       quiz = models.ForeignKey(Quiz,on_delete= models.CASCADE)
       score = models.IntegerField()
       user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
       submited_at = models.DateTimeField(auto_now_add=True)
       def __str__(self):
              return self.quiz.title	

class Plans(models.Model):
       pid = models.BigAutoField(primary_key=True) 
       name = models.CharField(max_length=20,null=False)
       amount = models.IntegerField()
       created_at = models.DateTimeField(auto_now_add=True)
       def __str__(self):
              return self.name
       
class Order(models.Model):
       oid = models.BigAutoField(primary_key=True)
       user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
       plans = models.ForeignKey(Plans,on_delete=models.CASCADE)
       company = models.CharField(max_length=30,null=False)
       amount = models.IntegerField(null=False)
       razorpay_order_id = models.CharField(max_length=100,null=False)
       razorpay_payment_id = models.CharField(max_length=100,null=False,blank=True)
       razorpay_payment_signature = models.CharField(max_length=100,null=False,blank=True)
       def __str__(self):
              return self.company
       
class contactus(models.Model):
       cusid = models.BigAutoField(primary_key=True)
       name = models.CharField(max_length=60,null=False)
       number = models.IntegerField(null=False)
       email = models.EmailField(unique=True)
       body = models.CharField(max_length=100)
       inquiry_at = models.DateTimeField(auto_now_add=True)
       def __str__(self):
              return self.email

class quizInvite(models.Model):
       qIid = models.BigAutoField(primary_key=True)
       quiz = models.ForeignKey(Quiz,on_delete= models.CASCADE)
       college = models.CharField(max_length=100,null=False)
       branch = models.CharField(max_length=10,null=False,blank=True)
       passyear = models.IntegerField(null=False,blank=True)
       phone = models.BigIntegerField(null=False)
       country = models.CharField(max_length=100,null=False)
       user = models.ForeignKey(CustomUser,on_delete= models.CASCADE)
       invited_at = models.DateTimeField(auto_now_add=True)
       def __str__(self):
              return self.college