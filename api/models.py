from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Note(models.Model):
    owner = models.ForeignKey(User, related_name='notes',on_delete=models.CASCADE)
    body = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_date']

    def __str__(self):
        return f'{self.body[:50]}'