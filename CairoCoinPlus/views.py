from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse
from django.core.paginator import Paginator
from .models import *

def index(request):
    
    return render(request, "CairoCoinPlus/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "CairoCoinPlus/login.html", {
                "message": "- Invalid username or password -"
            })
    else:
        return render(request, "CairoCoinPlus/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if username == "" or email == "" or password == "" or confirmation == "":
            return render(request, "CairoCoinPlus/register.html", {
                "message": "- Please Complete All Data -"
            })
        
        if password != confirmation:
            return render(request, "CairoCoinPlus/register.html", {
                "message": "- Passwords must match -"
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "CairoCoinPlus/register.html", {
                "message": "- Username already taken -"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "CairoCoinPlus/register.html")