"""Users views modules."""

# Django modules
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.contrib.auth.decorators import login_required

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
    """signup view"""
    return render(request, "users/signup.html")