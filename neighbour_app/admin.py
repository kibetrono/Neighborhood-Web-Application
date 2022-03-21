from calendar import c
import django
from django.contrib import admin
from .models import Business,Category,UserProfile,Neighbourhood,Location,Contact,Post


# Register your models here.

admin.site.register(Business)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Neighbourhood)
admin.site.register(Location)
admin.site.register(Contact)
admin.site.register(Post)