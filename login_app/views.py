from datetime import datetime, timezone, timedelta
import time

from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, reverse
from login_app.models import PasswordResetRequest, UserProfile, Role


def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user_authenticated = authenticate(request, username=username, password=password)
        if user_authenticated:
            dj_login(request, user_authenticated)
            user = User.objects.get(username=username)
            user_profile = UserProfile.objects.get(user=user)
            return HttpResponseRedirect(reverse('product_management_app:select_storage'))
        else:
            context = {
                'error': 'Bad username or password',
            }

    return render(request, "login_app/login.html", context)


@login_required
def logout(request):
    dj_logout(request)
    return render(request, 'login_app/login.html')


def sign_up(request):
    context = {}
    if request.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        username = request.POST['username']
        email = request.POST['email_address']
        if not password == confirm_password:
            context = {
                'password_match_error': 'Password does not match'
            }
        else:
            if User.objects.create_user(username, email, password):
                user = User.objects.get(username=username)
                customer_role = Role.objects.get(role="customer")
                user_profile = UserProfile(user=user, role=customer_role)
                user_profile.save()
                return HttpResponseRedirect(reverse('login_app:login'))
            else:
                context = {
                    'error': 'Creation of user FAILED',
                }
    return render(request, 'login_app/sign_up.html', context)


# Creating a request for password reset by getting a random token connected to a link
def password_reset_request(request):
    if request.method == 'POST':
        if request.POST['email']:
            email = request.POST['email']
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                pass_reset_request = PasswordResetRequest.objects.create(user=user)
                print('http://127.0.0.1:8000/accounts/new-password?token=' + pass_reset_request.token)
        else:
            context = {
                'error': "Enter email please",
            }
            return render(request, 'login_app/password_reset_request.html', context)
    return render(request, 'login_app/password_reset_request.html')


# If GET request then template is presented
# If POST request then compare username with PasswordResetRequest model with given token and if success then change
# password to new password
def new_password(request):
    if request.method == 'GET':
        if request.GET['token']:
            token = request.GET['token']
            if PasswordResetRequest.objects.filter(token=token).exists():
                pass_reset_request = PasswordResetRequest.objects.get(token=token)
                now = datetime.now(timezone.utc)
                if (((now - pass_reset_request.created_timestamp).seconds / 60) / 60) < 1 and \
                        pass_reset_request.updated_timestamp == pass_reset_request.created_timestamp:
                    context = {
                        'token': token,
                    }
                    return render(request, 'login_app/new_password.html', context)
    if request.method == 'POST':
        if request.POST['token']:
            token = request.POST['token']
            if PasswordResetRequest.objects.filter(token=token).exists():
                pass_reset_request = PasswordResetRequest.objects.get(token=token)
                if pass_reset_request.user.username == request.POST['username'] and \
                        request.POST['password'] == request.POST['confirm_password'] and \
                        request.POST['password'].strip() != "":

                    pass_reset_request.save()
                    user = User.objects.get(username=request.POST['username'])
                    user.set_password(request.POST['password'])
                    user.save()

                    return HttpResponseRedirect(reverse('login_app:login'))
                else:
                    context = {
                        'error': 'Wrong username or passwords does not match',
                        'token': token,
                    }
                    return render(request, 'login_app/new_password.html', context)
    raise Http404


@login_required
def delete_account(request):
    user = User.objects.get(username=request.POST['username'])
    user.delete()
    user.save()
    return HttpResponseRedirect(reverse('login_app:login'))
