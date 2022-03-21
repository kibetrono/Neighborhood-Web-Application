
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
 

    
@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    profile = UserProfile.objects.filter(user_id=current_user.id).first() 
    posts = Post.objects.filter(user_id=current_user.id)
    locations = Location.objects.all()
    neighbourhood = Neighbourhood.objects.all()
    category = Category.objects.all()
    businesses = Business.objects.filter(user_id=current_user.id)
    contacts = Contact.objects.filter(user_id=current_user.id)
    context={'profile': profile, 'posts': posts, 'locations': locations, 'neighbourhood': neighbourhood, 'categories': category, 'businesses': businesses, 'contacts': contacts}
    return render(request, 'neighbour_app/new_profile.html', context)


@login_required(login_url='/accounts/login/')
def update_profile_form(request):
    neighbourhood = Neighbourhood.objects.all()
    locations = Location.objects.all()
    context={'locations': locations, 'neighbourhood': neighbourhood}
    return render(request, 'neighbour_app/updateProfile.html',context)
