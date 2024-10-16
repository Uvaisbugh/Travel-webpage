from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,"login.html")

from django.utils.datastructures import MultiValueDictKeyError

def register(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
        except MultiValueDictKeyError:
            messages.error(request, "All fields are required")
            return redirect('register')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is already taken")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is already registered")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, "Account created successfully! You can now log in.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    
    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')