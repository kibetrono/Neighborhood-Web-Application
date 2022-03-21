from django.test import TestCase
from .models import Post, Category, UserProfile, Location, Neighbourhood, Business, Contact
from django.contrib.auth.models import User


class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Test Location')
        self.location.save_location()
        self.admin = User.objects.create_superuser(username='developer',password='password')
        self.neighbourhood = Neighbourhood(name='Test Neighbourhood', location=self.location, occupants_count=100, admin_id=self.admin.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))

    def test_save_method(self):
        self.neighbourhood.save_neigborhood()
        neighbourhoods = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhoods) > 0)

    def test_delete_method(self):
        self.neighbourhood.save_neigborhood()
        self.neighbourhood.delete()
        neighbourhoods = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhoods) == 0)


class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Test Location')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.location.save_location()
        self.location.delete()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='Test Category')

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_method(self):
        self.category.save()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_method(self):
        self.category.save()
        self.category.delete()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)


