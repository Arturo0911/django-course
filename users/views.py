"""Users views modules."""

# Django modules
from users.models import Profile
from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.contrib.auth.decorators import login_required

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User

# Forms
from users.forms import ProfileForm

def index_view(request):
    return HttpResponse("The index route")



def login_view(request):
    """login authentication"""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user  = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("feed")
        else:
            return render(request, "users/login.html", {"error": "Invalid username or password"})

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect("login")



def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')


@login_required
def update_profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data["website"]
            profile.phone_number = data["phone_number"]
            profile.biography = data["biography"]
            profile.picture = data["picture"]
            profile.save()
            print(form.cleaned_data)
            
            return redirect("feed")
    else:
        form = ProfileForm()
    

    
    return render(
        request= request, 
        template_name="users/update_profile.html",
        context={
                "profile": profile,
                "user": request.user
            }
        )