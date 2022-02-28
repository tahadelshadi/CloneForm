from django import forms
from .models import Answer, Question ,Choice, Response,Form
from django.forms import modelformset_factory


class CreateBaseForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ('title','description',)

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title','q_type','required')
    widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Book Name here'
                }
            )
        }

ChoiceFormset = modelformset_factory(
    Choice,
    fields=('text', ),
    extra=4,
    widgets={'text': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'جواب فرم ست'
        })
    }
)

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = '__all__'

