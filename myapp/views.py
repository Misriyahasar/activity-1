from django.shortcuts import render

# Create your views here.
from .models import Question

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'myapp/question_list.html', {'questions': questions})

def choice_list(request, pk):
    question = Question.objects.get(pk=pk)
    return render(request, 'myapp/choice_list.html', {'question': question})
