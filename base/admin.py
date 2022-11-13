from django.contrib import admin
from .models import ContactHeartCharity
# Register your models here.
@admin.register(ContactHeartCharity)
class ContactHeartCharityAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','last_name', 'email')
    list_display_links = ('id', 'first_name','last_name', 'email')
    search_fields = ('first_name','last_name', 'email')
    list_per_page = 25

