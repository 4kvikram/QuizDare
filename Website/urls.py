
from . import views
from django.urls import path


urlpatterns = [
    path('', views.Index, name="index"),
    path('<int:id>/', views.Index, name="index"),
    path('Selectquestion', views.Selectquestion, name="Selectquestion"),
    path('getAllQuestionAndOptions', views.getAllQuestionAndOptions,name="getAllQuestionAndOptions"),
    path('AddUserAndQuestion', views.AddUserAndQuestion, name="AddUserAndQuestion"),
    path('getUserQuestions', views.getUserQuestions, name="getUserQuestions"),
    path('saveResult', views.saveResult, name="saveResult"),
    path('getFriendsAnswerbyId', views.getFriendsAnswerbyId, name="getFriendsAnswerbyId"),
    path('submitContactUs', views.submitContactUs, name="submitContactUs"),
    path('contact', views.contact, name="contact"),
    path('game', views.Game, name="game"),


    
]
