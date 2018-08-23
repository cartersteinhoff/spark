
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Trip


def index(request):
    return render(request, 'spark_app/index.html')


def login(request):
    return render(request, 'spark_app/login.html')


def process_login(request):
    pending_user = User.objects.validate_login(request.POST)
    if pending_user['status']:  # if user is logged in
        request.session['user_id'] = pending_user
        return redirect('/success')
    else:
        for error in pending_user['errors']:
            messages.error(request, error)
    return redirect('/')


def process_registration(request):
    # Validate User
    pending_user = User.objects.validate_registration(request.POST)
    if pending_user['status']:  # if user is logged in
        request.session['user_id'] = pending_user['user_id']
        return render(request, 'spark_app/success.html')
    else:
        for error in pending_user['errors']:
            messages.error(request, error)
            print(error)
        return redirect(register)


def register(request):
    return render(request, 'spark_app/register.html')


def create_trip_process(request):
    new_trip = Trip.objects.validate_trip(request.POST)
    return render(request, 'spark_app/dashboard.html')
