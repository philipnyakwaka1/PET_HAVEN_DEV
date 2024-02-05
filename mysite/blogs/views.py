from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Blog Homepage')


def blog(request):
    return HttpResponse("Philip's blog")
