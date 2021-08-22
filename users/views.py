"""Users views modules."""

# Django modules
from django.shortcuts import redirect, render
from django.contrib.auth import (
    authenticate,
    login
)

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
            render(request, "users/login.html", {"error": "Invalid username or password"})

    return render(request, "users/login.html")

# Create your views here.
