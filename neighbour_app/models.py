from django.db import models
from datetime import datetime as dt
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-updated_at','-created_at']

    def save_category(self):
        self.save()

    def update_category(self,name,description):
        self.name=name
        self.description=description
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-updated_at','-created_at']

    def save_location(self):
        self.save()


    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name