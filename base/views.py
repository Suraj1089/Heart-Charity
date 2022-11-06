from django.shortcuts import render
from .models import ContactHeartCharity
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# from django.core.validators import validate_email

# Create your views here.


def is_valid_email(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def home(request):
    return render(request, 'index.html')


def donate(request):
    return render(request, 'donate.html')


def news(request):
    return render(request, 'news.html')


def news_detail(request):
    return render(request, 'news-detail.html')


def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        message = request.POST['message']
        print(first_name, last_name, email, message)

        if is_valid_email(email):
            contactHeartCharity = ContactHeartCharity(
                first_name=first_name, last_name=last_name, email=email, message=message)
            contactHeartCharity.save()
            send_mail(
                'Heart Charity Contact Form',
                'Thank you for contacting Heart Charity. We will get back to you as soon as possible.',
                email,
                ['surajpisal113@gmail.com'],
                fail_silently=False,
            )
            messages.success(
                request, 'Your message has been sent. Thank you for contacting us.')
            return HttpResponseRedirect('/contact/')
        if not is_valid_email(email):
            messages.error(request, 'Please enter a valid email address.')

    return render(request, 'index.html')
