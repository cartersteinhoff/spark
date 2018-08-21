
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages


def index(request):
    return render(request, 'spark_app/index.html')


def success(request):
    return render(request, 'spark_app/success.html')
