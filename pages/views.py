from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views import View

def home(request):
    return render(request, 'home.html',)


def chat(request):
    return render(request, 'chat.html',)


def status(request):
    return render(request, 'status.html',)

def calls(request):
    return render(request, 'calls.html',)

def communities(request):
    return render(request, 'communities.html',)