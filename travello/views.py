from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Destination
from django.contrib import messages
# Create your views here.
def index(request):
    dests = Destination.objects.all()
    return render(request, "index.html", {'dests': dests})

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def registration(request):

    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exist():
                messages.info(request, 'username taken')
                return redirect('registration')
            elif User.objects.filter(email=email).exist():
                messages.info(request, 'email taken')
                return redirect('registration')
            else:
                user=User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'password not matching')
            return redirect('registration')

        return redirect('/')
    else:
        return render(request, "registration.html")