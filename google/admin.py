from pyexpat import model
from django.contrib import admin
from .models import Answer, Choice, Form,Question, Response, User

class FormAdmin(admin.ModelAdmin):
    model = Form
    ordering = ['pk']

class QuestionAdmin(admin.ModelAdmin):
    model = Question
    ordering = ['pk']


admin.site.register(User)    
admin.site.register(Form,FormAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Choice)
admin.site.register(Response)

