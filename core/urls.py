from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('about/',views.about,name='about'),
   path('docs/',views.documentation,name='docs'),
   path('contact/',views.contact_us,name='contact'),
   path('postUpload/',views.postUpload,name='postUpload'),
   path('success',views.success,name='success'),
   path('postEdit/<int:pk>/',views.postEdit,name='postEdit'),
   path('conformPost/<int:pk>/',views.conformPostForDelete,name='conformPost'),
   path('postDelete/<int:pk>/',views.postDelete,name='postDelete'),
   path('questionUpload/',views.questionUpload,name='questionUpload'),
   path('questionEdit/<int:pk>/',views.questionEdit,name='questionEdit'),
   path('conformQuestionForDelete/<int:pk>/',views.comformQuestionForDelete,name='conformQuestionForDelete'),
   path('deleteQuestion/<int:pk>/',views.deleteQuestion,name='deleteQuestion'),
   path('answerUpload/<int:pk>/',views.answerUpload,name='answerUpload'),
   path('answerEdit/<int:pk>/',views.answerEdit,name='answerEdit'),
   path('conformAnswerForDelete/<int:pk>/',views.conformAnswerForDelete,name='conformAnswerForDelete'),
   path('answerDelete/<int:pk>/',views.answerDelete,name='answerDelete'),
   path('problemUpload/',views.problemUpload,name='problemUpload'),
   path('problemEdit/<int:pk>/',views.problemEdit,name='problemEdit'),
   path('conformProblemForDelete/<int:pk>/',views.conformProblemForDelete,name='conformProblemForDelete'),
   path('problemDelete/<int:pk>/',views.problemDelete,name='problemDelete'),
   path('answerForProblemUpload/',views.answerForProblemUpload,name='answerForProblemUpload'),
   path('answerForProblemEdit/<int:pk>/',views.answerForProblemEdit,name='answerForProblemEdit'),
   path('conformAnswerForProblemForDelete/<int:pk>/',views.conformAnswerForProblemForDelete,name='conformAnswerForProblemForDelete'),
   path('answerForProblemDelete/<int:pk>/',views.answerForProblemDelete,name='answerForProblemDelete'),
   path('quizUpload/',views.quizUpload,name='quizUpload'),
   path('quizEdit/<int:pk>/',views.quizEdit,name='quizEdit'),
   path('conformQuizForDelete/<int:pk>/',views.conformQuizForDelete,name='conformQuizForDelete'),
   path('quizDelete/<int:pk>/',views.quizDelete,name='quizDelete'),
   path('singlepost/<int:pk>/',views.singlepost,name='singlepost'),
   path('displayAllQuiz/',views.displayAllQuiz,name='displayAllQuiz'),
   path('displayQuiz/<int:pk>/',views.diplayQuiz,name='displayQuiz'),
   path('submitAnswer/<int:qid>/<int:quid>/',views.submitAnswer,name='submitAnswer'),
   path('quizResult/<int:quid>/',views.quizResult,name='quizResult'),
   path('controlPanelForQuizManage/',views.controlPanelForQuizManage,name='controlPanelForQuizManage'),
   path('allQuizPageForQuizManage/',views.allQuizPageForQuizManage,name='allQuizPageForQuizManage'),
   path('QuizSubmissionPageForQuizManage/',views.QuizSubmissionPageForQuizManage,name='QuizSubmissionPageForPageQuizManage'),
   path('QuizResultPageForQuizManage/',views.QuizResultPageForQuizManage,name='QuizResultPageForQuizManage'),
   path('code/',views.code_Editor,name='code'),
] 


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)