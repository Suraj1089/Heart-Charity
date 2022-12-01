from django.shortcuts import render
from .models import ContactHeartCharity
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.conf import settings
import requests
# Create your views here.

GOOGLE_RECAPTCHA_SECRET_KEY = settings.GOOGLE_RECAPTCHA_SECRET_KEY
GOOGLE_RECAPTCHA_SITE_KEY = settings.GOOGLE_RECAPTCHA_SITE_KEY


def test(request):

    return render(request, 'test.html', {'recaptcha_site_key': GOOGLE_RECAPTCHA_SITE_KEY})


def is_valid_email(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def home(request):
    return render(request, 'index.html', {'recaptcha_site_key': GOOGLE_RECAPTCHA_SITE_KEY})


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

            recapcha_response = request.POST['g-recaptcha-response']
            data = {
                'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recapcha_response
            }
            print(data)
            r = requests.post(
                'https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            print(result)
            if result['success']:
                # send email
                try:
                    send_mail(
                        'Heart Charity Contact Form',
                        'Message from ' + first_name + ' ' + last_name + ' ' + message,
                        email, ['surajpisal113@gmail.com', ]
                    )
                    messages.add_message(
                        request, messages.SUCCESS, 'Your message has been sent successfully')
                except BadHeaderError:
                    messages.add_message(
                        request, messages.ERROR, 'Invalid header found')
                    return render(request, 'index.html')
            else:
                messages.add_message(
                    request, messages.ERROR, 'Invalid reCAPTCHA. Please try again.')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Invalid email address')

    return render(request, 'index.html')
