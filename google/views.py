from random import choice
from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Answer, Form, Question, Response , Choice
from .forms import CreateBaseForm, AnswerForm, QuestionForm, ChoiceFormset

# def formtest(request):
#     if request.method == 'GET':
#         questionForm = QuestionForm(request.GET or None)
#         formset = ChoiceFormset(queryset=Choice.objects.none())
#     if request.method == 'POST':
#         questionForm = QuestionForm(request.POST or None)
#         formset = ChoiceFormset(request.POST or None)
#         if formset.is_valid() and questionForm.is_valid():
#             question = questionForm.save()
#             for form in formset:
#                 choice = form.save(commit=False)
#                 choice.question = question
#                 choice.save()
#             return redirect('home')
#     context= {
#         'formset': formset,
#         'questionForm':questionForm,

#     }
#     return render(request, 'form/formtest.html',context)

def home(request):

    form = CreateBaseForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.creator = request.user
            new_form.save()
            return redirect("google:create_form", pk = new_form.id)
        else:
            messages.error(request, "nashod")
            new_form = CreateBaseForm()
            return render(request, "form/home.html", context={
                "form": form
            })

    context={
        'form':form,
    }
    return render(request,'form/home.html',context)

def CreateForm(request, pk):
    form = Form.objects.get(id=pk)
    questions = form.questions.all()
    
    questionsform = QuestionForm(request.POST or None)
    if request.method == "POST":
        if questionsform.is_valid():
            question = questionsform.save()
            form.questions.add(question)
            return redirect("google:detail-question", pk = question.id)
        else:
            messages.error(request, "nashod")
            questionsform = QuestionForm()
            formset = ChoiceFormset()
            return render(request, "form/form.html", context={
                "questionsform": questionsform,
                'formset':formset,
            })

    context = {
        'questionsform': questionsform,
        'questions': questions,
        'form':form,
        }
    return render(request, 'form/form.html', context)

def DeleteForm(request, pk):
    form = get_object_or_404(Form, id=pk)
    #delete choice and questions####################################
    if request.method == "POST":
        form.delete()
        return redirect('google:home')

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )

def CreateQuestionForm(request):
    form = QuestionForm()
    context = {
        "form": form,
    }
    return render(request, "form/questionform.html", context)


def UpdateQuestion(request, pk):
    question = Question.objects.get(id=pk)
    choices = question.choices.all()

    form = QuestionForm(request.POST or None, instance=question)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("google:detail-question", pk=question.id)

    context = {
        "form": form,
        "question": question,
        'choices':choices,
    }

    return render(request, "form/questionform.html", context)


def DeleteQuestion(request, pk):
    question = get_object_or_404(Question, id=pk)

    if request.method == "POST":
        question.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )

def DetailQuestion(request,pk):
    question = get_object_or_404(Question, id=pk)

    context = {
        "question": question
    }
    return render(request, "form/questiondetail.html", context)

def ChoiceForm(request,pk):
    question = Question.objects.get(id=pk)
    choices = question.choices.all()

    choiceform = ChoiceForm(request.POST or None,instance = choices)
    if request.method == "POST":
        if choiceform.is_valid():
            choice = choiceform.save(commit=False)
            choice.save()
            question.choices.add(choice)
            # return redirect("detail-question", id = question.id)
            return redirect("google:detail-choice", id = choice.id)
        else:
            messages.error(request, "nashod")
            choice = ChoiceForm()
            return render(request, "form/create_choice.html", context={
                "choiceform": choiceform
            })
    context = {
        'question': question,
        'choices': choices,
       
    }
    return render(request, 'form/test.html', context)


def CreateChoiceForm(request):
    form = QuestionForm()
    context={
        'form':form,
    }
    return render(request, "form/choiceform.html", context)

def DetailChoice(request, pk):
    choice = get_object_or_404(Choice, id=pk)
    context = {
        "choice": choice
    }
    return render(request, "form/choicedetail.html", context)

def UpdateChoice(request, pk):
    choice = Choice.objects.get(id=pk)

    form = ChoiceForm(request.POST or None, instance=choice)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("google:detail-question", pk=choice.id)

    context = {
        "form": form,
        'choice':choice,
    }

    return render(request, "form/questionform.html", context)


def DeleteChoice(request, pk):
    choice = get_object_or_404(Choice, id=pk)

    if request.method == "POST":
        choice.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )

def CreateResponse(request,pk):
    my_form = Form.objects.get(id=pk) 
    questions = my_form.questions.all()
    # choices = questions.get_choices()
    # for choice in questions:
    #     print(choice.choices.text)
    #     choices = choice

    answerform = AnswerForm(request.POST or None)
    if request.method == "POST":
        if answerform.is_valid():
            form = answerform.save(commit=False)
            answerform(answer_to=questions)
            form.save()
            Response.create(responder=request.user,response_to=my_form,response=Response.join(answerform))
            return redirect("google:home")
        else:
            messages.error(request, "nashod")
            form = AnswerForm()
            return render(request, "form/create_form.html", context={
                "answerform": answerform
            })
    context = {
        'my_form':my_form,
        'questions':questions,
        # 'choices':choices,
        'answerform':answerform,
    }
    return render(request,'form/response.html',context)
# pk = responder id 
def ResponseFormDetail(request,pk):
    my_form = Form.objects.get(id=pk) 
    questions = my_form.questions.all()
    response = Response.objects.filter(answer=questions)
    for res in response:
        print(res)
    context = {
        'my_form':my_form,
        'questions':questions,
        'response':response,
    }
    return render(request,'form/response.html',context)
