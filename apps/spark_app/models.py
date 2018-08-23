from django.db import models
import bcrypt
import datetime

# Create your models here.

# User Model


class UserManager(models.Manager):
    def validate_registration(self, postData):
        response = {
            'status': False,
            'errors': []
        }

<<<<<<< HEAD
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
=======
        if len(postData['first_name']) < 2:
            response['errors'].append("First Name Too Short")

        if len(postData['last_name']) < 2:
            response['errors'].append("Last Name Too Short")

        if len(postData['email']) < 5:
            response['errors'].append("Email Too Short")

        if len(postData['password']) < 5:
            response['errors'].append("Password Too Short")

        if postData['confirm_password'] != postData['password']:
            response['errors'].append("Password needs to be the same")

        if len(response['errors']) == 0:
            response['status'] = True
            response['user_id'] = User.objects.create(
                first_name=postData['first_name'],
                last_name=postData['last_name'],
                email=postData['email'],
                password=postData['password']
                # password=bcrypt.hashpw(
                #     postData['password'].encode('utf-8'), bcrypt.gensalt())
            ).id
        print(response)
        return response

    def validate_login(self, postData):
        response = {
            'status': False,
            'errors': []
        }
        # See if email already exists
        existing_user = User.objects.filter(email=postData['email'])
        if len(existing_user) == 0:
            print('errors')
            response['errors'].append("invalid input")
        if postData['password'] == existing_user[0].password:
            # Compare Form Input Password to DB
            # if bcrypt.checkpw(postData['password'].encode('utf-8'), existing_user[0].password.encode('utf-8')):
            response['status'] = True
            response['user_id'] = existing_user[0].id
            print('works')
        else:
            print("invalid input")
        return response


class User(models.Model):
    print('user created')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# Trip Model


class TripManager(models.Manager):
    def validate_trip(self, postData):
        response = {
            'status': False,
            'errors': []
        }

        response['status'] = True
        response['trip_id'] = Trip.objects.create(
            destination=postData['destination'],
            description=postData['description'],
            travel_date_from=postData['travel_date_from'],
            travel_date_to=postData['travel_date_to'],
        )

        return response


class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    travel_date_from = models.DateField(null=True)
    travel_date_to = models.DateField(null=True)
    created_by = models.ForeignKey(
        User, related_name="created_trips", on_delete=models.CASCADE, null=True)
    user_on_trip = models.ManyToManyField(
        User, related_name="trips")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()
>>>>>>> 115cf0fc419771cb653b0b131549c4779e70f709
