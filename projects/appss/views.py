import objects as objects
from django.contrib import auth
from django.core.checks import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        uname = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        spassword = request.POST['spassword']
        if password == spassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'user name is already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=uname, email=email, password=password)
                user.save()
        else:
            messages.info(request, "password is not matching")
            return redirect('signup')
        return redirect('signup')

    return render(request, 'signup.html')
def signin(request):
    if request.method == "POST":
        Username = request.POST['Username']
        password = request.POST['password']
        user = auth.authenticate(username=Username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'invalid credential')
            return redirect('home')
    return render(request, 'signin.html')
