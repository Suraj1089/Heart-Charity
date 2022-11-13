from django.shortcuts import render
import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
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
        confirm_password = request.POST['confirm_password']

        if is_valid_email(email):
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already taken')
                    return redirect('signup')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email already taken')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(
                        username=username, email=email, password=password)
                    user.save()
                    return redirect('login')
            else:
                messages.info(request, 'Password not matching')
                return redirect('signup')
        else:
            messages.info(request, 'Invalid email')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_user(request):
    auth.logout(request)
    messages.success(request, 'Logout successful')
    return redirect('home')
