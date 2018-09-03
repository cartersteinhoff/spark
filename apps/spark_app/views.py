
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Trip
from django.http import JsonResponse


def json_payload(response):
    data = list(Trip.objects.values())
    data_new = Trip.objects.all()
    carter = {
        'name': '',
        'age': '',
        'zip': '',
    }

    for key in carter:
        print(key)
        carter[key] = 1
    print(carter)
    # for item in carter:
    #     print(item.destination)
    return JsonResponse(carter, safe=False)


def index(request):

    context = {
        'all_trips': Trip.objects.all()
    }

    return render(request, 'spark_app/index.html', context)


def login(request):
    return render(request, 'spark_app/login.html')


def logout(request):
    del request.session['user_id']
    return redirect(index)


def process_login(request):
    pending_user = User.objects.validate_login(request.POST)
    if pending_user['status']:  # if user is logged in
        request.session['user_id'] = pending_user['user_id']
        return redirect(dashboard)
    else:
        for error in pending_user['errors']:
            messages.error(request, error)
    return redirect('/')


def process_registration(request):
    # Validate User
    pending_user = User.objects.validate_registration(request.POST)
    if pending_user['status']:  # if user is logged in
        request.session['user_id'] = pending_user['user_id']
        return redirect(dashboard)
    else:
        for error in pending_user['errors']:
            messages.error(request, error)
            print(error)
        return redirect(register)


def register(request):
    return render(request, 'spark_app/register.html')

# Trips


def create_trip(request):
    return render(request, 'spark_app/create_trip.html')


def process_create_trip(request):

    new_trip = Trip.objects.create_trip(
        request.POST, request.session['user_id'])

    return redirect(dashboard)


def join_trip(request, trip_id):

    user_trip = Trip.objects.join(trip_id, request.session['user_id'])

    return redirect(dashboard)


# Dashboard

def dashboard(request):

    context = {
        "all_trips":  Trip.objects.all(),
        "user_trips": User.objects.get(id=request.session['user_id']).created_trips.all()
    }
    return render(request, 'spark_app/dashboard.html', context)
