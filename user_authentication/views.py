from django.shortcuts import render
import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# import login required decorator
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings

GOOGLE_RECAPTCHA_SECRET_KEY = settings.GOOGLE_RECAPTCHA_SECRET_KEY
GOOGLE_RECAPTCHA_SITE_KEY = settings.GOOGLE_RECAPTCHA_SITE_KEY


def is_valid_email(email: str) -> bool:
    if email and re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False


def signup_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password2']

        if is_valid_email(email):
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.add_message(
                        request, messages.ERROR, 'Username already exists')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.add_message(
                        request, messages.ERROR, 'Email already exists')
                    return redirect('register')
                else:
                    # check captcha is valid or not
                    recapcha_response = request.POST['g-recaptcha-response']
                    # print(recapcha_response)
                    data = {
                        'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
                        'response': recapcha_response
                    }
                    # print(data)
                    r = requests.post(
                        'https://www.google.com/recaptcha/api/siteverify', data=data)
                    result = r.json()
                    # print(result)
                    if result['success']:
                        user = User.objects.create_user(
                            username=username, email=email, password=password)
                        user.save()
                        messages.success(request, 'User created successfully')
                        return redirect('login')
                    else:
                        messages.add_message(
                            request, messages.ERROR, 'Invalid captcha')
                        return redirect('register')
            else:
                messages.add_message(
                    request, messages.ERROR, 'Password does not match')
                return redirect('register')
        else:
            messages.add_message(
                request, messages.ERROR, 'Invalid email')
            return redirect('register')
    else:
        return render(request, 'user_authentication/register.html', {'recaptcha_site_key': GOOGLE_RECAPTCHA_SITE_KEY})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # auth user and check capthca
        user = auth.authenticate(username=username, password=password)

        # check captcha is valid or not
        recapcha_response = request.POST['g-recaptcha-response']
        # print(recapcha_response)
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recapcha_response
        }
        # print(data)
        r = requests.post(
            'https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        # print(result)
        if result['success']:
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login successful')
                return redirect('home')
            else:
                messages.add_message(
                    request, messages.ERROR, 'Invalid credentials')
                return redirect('login')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid captcha')
            return redirect('login')
    else:
        return render(request, 'user_authentication/login.html', {'recaptcha_site_key': GOOGLE_RECAPTCHA_SITE_KEY})


def logout_user(request):
    auth.logout(request)
    messages.success(request, 'Logout successful')
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'user_authentication/dashboard.html', {'recaptcha_site_key': GOOGLE_RECAPTCHA_SITE_KEY})


@login_required(login_url='login')
def update_profile(request):
    return render(request, 'user_authentication/update_profile.html', {'recaptcha_site_key': GOOGLE_RECAPTCHA_SITE_KEY})
