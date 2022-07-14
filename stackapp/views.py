import imp
from django.views.generic import ListView
from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.
def display(request):
    s='<h1>Hello Welcome to Heroku Server!!!</h1>'
    return render(request,'Home.html')

def about(request):
    return render(request,'About.html')

class QuestionListView(ListView):
    model = Question
