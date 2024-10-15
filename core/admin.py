from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

class QuestionForQuiz(admin.StackedInline):
    model = Question

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionForQuiz]


admin.site.register(Question,QuestionAdmin)

admin.site.register(Answer)
admin.site.register(Problem)
admin.site.register(AnswerForProblem)
admin.site.register(Quiz,QuizAdmin)
admin.site.register(QuizSubmit)
admin.site.register(Order)
admin.site.register(Plans)
admin.site.register(contactus)
admin.site.register(quizInvite)