from django.contrib import admin
from .models import Profile
# import format_html
from django.utils.html import format_html

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # render photo
    def image_url(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.image.url))
    
    list_display = ('user', 'image_url', 'bio', 'address', 'city', 'state', 'country', 'zip_code', 'phone')