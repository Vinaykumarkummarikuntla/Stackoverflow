from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def display(request):
    s='<h1>Hello Welcome to Heroku Server!!!</h1>'
    return render(request,'Home.html')
