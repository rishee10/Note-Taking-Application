import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    name=models.TextField(blank=True)
    name1=models.CharField(max_length=128, null=True)
    age=models.CharField(max_length=128, null=True)

    
    def __str__(self):
        return self.name1