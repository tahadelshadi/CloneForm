from django.urls import path
from . import views


app_name= "google"
urlpatterns = [
    path('', views.home, name="home"),
    path('createform/<pk>/', views.CreateForm, name="create_form"),
    path('delete/<pk>/', views.DeleteForm, name="delete-form"),
    # questions
    path('create_question_form/', views.CreateQuestionForm, name="create_question_form"),
    path('question/<pk>/', views.DetailQuestion, name="detail-question"),
    path('question/<pk>/update/', views.UpdateQuestion, name="update-question"),
    path('question/<pk>/delete/', views.DeleteQuestion, name="delete-question"),
    #choice
    path('choice/<pk>/', views.CreateChoiceForm, name="create-choice-form"),
    # path('choice/<pk>', views.ChoiceForm, name="detail-choice"),
    path('question/<pk>/', views.DetailChoice, name="detail-choice"),
    #response
    path('answer/<pk>/', views.CreateResponse, name="answer-form"),
    path('response/<pk>/', views.ResponseFormDetail, name="Response-Detail"),
    
    

    # path('test/', views.formtest, name="form-test"),
]
