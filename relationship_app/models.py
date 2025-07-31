from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):  # Required exact line
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [             # Keep order and spacing simple
        ('Admin', 'Admin'),      # Must include these EXACT strings
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"



class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
