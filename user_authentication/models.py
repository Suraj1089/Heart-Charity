from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    # birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    resume = models.FileField(upload_to='resume', blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    
    def resume_url(self):
        if self.resume and hasattr(self.resume, 'url'):
            return self.resume.url
    