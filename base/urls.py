from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('test/', views.test, name="test"),
    path('volunteer/', views.voluteer_form, name="volunteer"),
    
    
]