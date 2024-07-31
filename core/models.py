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
       def __str__(self):
              return self.title       

class Question(models.Model):
       qid = models.BigAutoField(primary_key=True)
       category = models.ForeignKey(Category,on_delete= models.CASCADE) 
       quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
       question = models.CharField(max_length=100)
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