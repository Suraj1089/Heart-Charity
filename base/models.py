from django.db import models

# Create your models here.

class ContactHeartCharity(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    