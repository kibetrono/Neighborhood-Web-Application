
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Business,Category,UserProfile,Neighbourhood,Location,Contact,Post
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
        all_posts = Post.objects.all().order_by("-created_at")
        context={'posts': all_posts}
        return render(request, 'neighbour_app/home.html', context)
 