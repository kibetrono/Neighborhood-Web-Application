
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

@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == "POST":
        current_user = request.user
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        name = request.POST["first_name"] + " " + request.POST["last_name"]
        neighbourhood = request.POST["neighbourhood"]
        location = request.POST["location"]
        if location == "":
            location = None
        else:
            location = Location.objects.get(name=location)

        if neighbourhood == "":
            neighbourhood = None
        else:
            neighbourhood = Neighbourhood.objects.get(name=neighbourhood)
        profile_image = request.FILES["profile_pic"]
        profile_image = cloudinary.uploader.upload(profile_image)
        profile_url = profile_image["url"]
        user = User.objects.get(id=current_user.id)
        if UserProfile.objects.filter(user_id=current_user.id).exists():

            profile = UserProfile.objects.get(user_id=current_user.id)
            profile.profile_pic = profile_url
            profile.neighbourhood = neighbourhood
            profile.location = location
            profile.save()
        else:
            profile = UserProfile(user_id=current_user.id,name=name,profile_pic=profile_url,neighbourhood=neighbourhood,location=location,)

            profile.save_userProfile()

        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        user.save()

        return redirect("/profile",)

    else:
        return render(request, "neighbour_app/new_profile.html")


@login_required(login_url='/accounts/login/')
def addPost(request):
    locations = Location.objects.all()
    category = Category.objects.all()
    context={'locations': locations,  'categories': category}
    return render(request, 'neighbour_app/addpost.html',context)

@login_required(login_url='/accounts/login/')
def addBusiness(request):
    context={}
    return render(request, 'neighbour_app/addbusiness.html',context)

@login_required(login_url='/accounts/login/')
def addContact(request):
    context={}
    return render(request, 'neighbour_app/addcontact.html',context)


# create post
@login_required(login_url="/accounts/login/")
def new_post(request):
    if request.method == "POST":
        current_user = request.user
        title = request.POST["title"]
        content = request.POST["content"]
        category = request.POST["category"]
        location = request.POST["location"]
        profile = UserProfile.objects.filter(user_id=current_user.id).first()
        
        if category == "":
            category = None
        else:
            category = Category.objects.get(name=category)

        if location == "":
            location = None
        else:
            location = Location.objects.get(name=location)

        if request.FILES:
            image = request.FILES["image"]
            image = cloudinary.uploader.upload(image, crop="limit", width=800, height=600)
            image_url = image["url"]

            post = Post(user_id=current_user.id,title=title,content=content,image=image_url,category=category,location=location)
            post.save_post()

            return redirect("/profile")
        else:
            post = Post(user_id=current_user.id,title=title,content=content,category=category,location=location)
            post.save_post()

            return redirect("/profile")

    else:
        return render(request, "neighbour_app/new_profile.html")


@login_required(login_url="/accounts/login/")
def save_business(request):
    if request.method == "POST":
        current_user = request.user
        name = request.POST["name"]
        email = request.POST["email"]

        profile = UserProfile.objects.filter(user_id=current_user.id).first()
        if profile is None:
            profile = UserProfile.objects.filter(
                user_id=current_user.id).first()  
            posts = Post.objects.filter(user_id=current_user.id)
            locations = Location.objects.all()
            neighbourhood = Neighbourhood.objects.all()
            category = Category.objects.all()
            businesses = Business.objects.filter(user_id=current_user.id)
            contacts = Contact.objects.filter(user_id=current_user.id)
            context={"locations": locations, "neighbourhood": neighbourhood, "categories": category, "businesses": businesses, "contacts": contacts, "posts": posts}
            return render(request, "neighbour_app/new_profile.html",context)
        else:
            neighbourhood = profile.neighbourhood

        if neighbourhood == "":
            neighbourhood = None
        else:
            neighbourhood = Neighbourhood.objects.get(name=neighbourhood)

        business = Business(user_id=current_user.id,name=name,email=email,neighbourhood=neighbourhood,)
        business.create_business()

        return redirect("/profile")
    else:
        return render(request, "neighbour_app/new_profile.html")


@login_required(login_url="/accounts/login/")
def save_contact(request):
    if request.method == "POST":
        current_user = request.user
        name = request.POST["name"]
        email = request.POST["email"]
        telephone = request.POST["telephone"]

        profile = UserProfile.objects.filter(user_id=current_user.id).first()
        if profile is None:
            profile = UserProfile.objects.filter(user_id=current_user.id).first() 
            posts = Post.objects.filter(user_id=current_user.id)
            locations = Location.objects.all()
            neighbourhood = Neighbourhood.objects.all()
            category = Category.objects.all()
            businesses = Business.objects.filter(user_id=current_user.id)
            contacts = Contact.objects.filter(user_id=current_user.id)
            context={ "locations": locations, "neighbourhood": neighbourhood, "categories": category, "businesses": businesses, "contacts": contacts, "posts": posts}
            return render(request, "neighbour_app/new_profile.html", context)
        else:
            neighbourhood = profile.neighbourhood

        if neighbourhood == "":
            neighbourhood = None
        else:
            neighbourhood = Neighbourhood.objects.get(name=neighbourhood)

        contact = Contact(user_id=current_user.id,name=name,email=email,telephone=telephone,neighbourhood=neighbourhood)
        contact.save_contact()

        return redirect("/profile",)
    else:
        return render(request, "neighbour_app/new_profile.html")


@login_required(login_url="/accounts/login/")
def alerts(request):
    current_user = request.user
    profile = UserProfile.objects.filter(user_id=current_user.id).first()
    if profile is None:
        profile = UserProfile.objects.filter(user_id=current_user.id).first()  
        posts = Post.objects.filter(user_id=current_user.id)
        locations = Location.objects.all()
        neighbourhood = Neighbourhood.objects.all()
        category = Category.objects.all()
        businesses = Business.objects.filter(user_id=current_user.id)
        contacts = Contact.objects.filter(user_id=current_user.id)
        context= {"locations": locations, "neighbourhood": neighbourhood, "categories": category, "businesses": businesses, "contacts": contacts, "posts": posts}
        return render(request, "neighbour_app/new_profile.html",context)
    else:
        neighbourhood = profile.neighbourhood
        category = Category.objects.get(name="alerts")
        posts = Post.objects.filter(neighbourhood=neighbourhood, category=category).order_by("-created_at")
        context={"posts": posts}
        return render(request, "neighbour_app/notifications.html", context)


@login_required(login_url="/accounts/login/")
def business(request):
    current_user = request.user
    profile = UserProfile.objects.filter(user_id=current_user.id).first()
    if profile is None:
        profile = UserProfile.objects.filter(
            user_id=current_user.id).first() 
        posts = Post.objects.filter(user_id=current_user.id)
        locations = Location.objects.all()
        neighbourhood = Neighbourhood.objects.all()
        category = Category.objects.all()
        businesses = Business.objects.filter(user_id=current_user.id)
        contacts = Contact.objects.filter(user_id=current_user.id)
        context= {"locations": locations, "neighbourhood": neighbourhood, "categories": category, "businesses": businesses, "contacts": contacts, "posts": posts}
        return render(request, "neighbour_app/new_profile.html",context)
    else:
        neighbourhood = profile.neighbourhood
        businesses = Business.objects.filter(neighbourhood=profile.neighbourhood)
        context={"businesses": businesses}
        return render(request, "neighbour_app/business.html", context)


@login_required(login_url="/accounts/login/")
def contacts(request):
    current_user = request.user
    profile = UserProfile.objects.filter(user_id=current_user.id).first()
    
    contacts = Contact.objects.all()
    context= {"contacts": contacts, "neighbourhood": profile.neighbourhood}
    return render(request, "neighbour_app/contacts.html",context)


@login_required(login_url="/accounts/login/")
def search(request):
    if 'query' in request.GET and request.GET["query"]:
        search_term = request.GET.get("query")
        searched_businesses = Business.objects.filter(name__icontains=search_term)
        message = f"Search For: {search_term}"
        context={"message": message, "businesses": searched_businesses}
        return render(request, "neighbour_app/search.html", context)
    else:
        message = "You haven't searched for any term"
        context= {"message": message}
        return render(request, "neighbour_app/search.html",context)
