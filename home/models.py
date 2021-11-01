from django.db import models
from django.db.models.fields import CharField

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.name