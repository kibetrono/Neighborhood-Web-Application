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

    def update_location(self,name):
        self.name=name
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name



class Neighbourhood(models.Model):
    name = models.CharField(max_length=70)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-updated_at','-created_at']


    def save_neigborhood(self):
        self.save()

    def update_neigborhood(self,name,location,occupants_count,admin):
        self.name=name
        self.location=location
        self.occupants_count=occupants_count
        self.admin=admin
        self.save()

    def delete_neigborhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_neighbourhood(cls, id):
        cls.objects.filter(id=id).update()

    @classmethod
    def search_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood


    def __str__(self):
        return self.name