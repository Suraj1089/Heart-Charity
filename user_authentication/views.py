from django.shortcuts import render
import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# import login required decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

# check email is in valid format or not


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
                    user = User.objects.create_user(
                        username=username, email=email, password=password)
                    user.save()
                    return redirect('login')
            else:
                messages.add_message(
                    request, messages.ERROR, 'Password does not match')
                return redirect('register')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid email')
            return redirect('register')
    else:
        return render(request, 'user_authentication/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Login successful')
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'user_authentication/login.html')


def logout_user(request):
    auth.logout(request)
    messages.success(request, 'Logout successful')
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'user_authentication/dashboard.html')


@login_required(login_url='login')
def update_profile(request):
    return render(request, 'user_authentication/update_profile.html')
