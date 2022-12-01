from django.db import models

# Create your models here.

class ContactHeartCharity(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    

class VolunteerForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    resume = models.FileField(upload_to='resume')
    

    def __str__(self):
        return self.first_name + ' ' + self.last_name