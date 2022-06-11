from django.shortcuts import render, redirect
from .forms import MyCreateUserForm
from django.contrib import messages
from base.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from cloudinary.forms import cl_init_js_callbacks

# Create your views here.

def home(request):
   context = {'title':'Awwwords - Home'}
   return render(request, 'home.html', context)
  
def loginPage(request):
   return render(request, 'login.html')
  
def registerPage(request):
   if request.user.is_authenticated:
       return redirect('home')
   form = MyCreateUserForm()
   context = {'form':form}
   if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists():
          messages.info(request, 'Username is taken')
          return redirect('registerPage')
        elif User.objects.filter(email=request.POST['email']).exists():
          messages.info(request, 'Email is taken')
          return redirect('registerPage')
        elif request.POST['password1'] != request.POST['password2']:
          messages.info(request, 'Password and Confirm Paswword dont match')
          return redirect('registerPage')
        else:
           form = MyCreateUserForm(request.POST)
           if form.is_valid():
               user = form.save(commit=False)
               user.username = user.username.lower()
               user.email = user.email.lower()
               user.save()
               # login(request, user)
               return redirect('home')       
           else:
             messages.error(request, 'An error ocurred during registration.')
          
   return render(request, 'register.html', context)


def profile(request):
   context = {'title':'Awwwords - Profile'}
   return render(request, 'profile.html', context)

def upload(request):
   context = {'title':'Awwwords - Upload'}
   return render(request, 'upload.html', context)

def post(request):
   context = {'title':'Awwwords - Post'}
   if request.method == 'POST':
      print(request.POST)
   return render(request, 'post.html', context)