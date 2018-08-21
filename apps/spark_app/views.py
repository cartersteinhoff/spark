
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User


def index(request):
    return render(request, 'spark_app/index.html')


def login(request):
    return render(request, 'spark_app/login.html')


def process_login(request):
    return redirect(login)


def register(request):
    return render(request, 'spark_app/register.html')


def process_register(request):
    # Validate User
    create_user = User.objects.validate_registration(request.POST)
    return redirect(register)
