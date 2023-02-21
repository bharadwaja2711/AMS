from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from .models import Image


def home(request):
    return render(request, 'users/home.html')

def aboutus(request):
    return render(request, 'users/aboutus.html')

def output1(request):
    return render(request, 'users/output1.html')

def creditcard(request):
    return render(request, 'users/creditcard.html')

def debitcard(request):
    return render(request, 'users/debitcard.html')

@login_required()
def buy(request):
    return render(request, 'users/buy.html')

@login_required()
def sell(request):
    return render(request, 'users/sell.html')

def upload(request):
    return render(request, 'users/upload.html')

def index(request):
    return render(request, 'users/index.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

@login_required()
def profile(request):
    return render(request, 'users/profile.html')
