from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('donate/', views.donate, name="donate"),
    path('news/', views.news, name="news"),
    path('news-detail/', views.news_detail, name="news-detail"),
    path('contact/', views.contact, name="contact"),
    path('test/', views.test, name="test"),
    
    
]