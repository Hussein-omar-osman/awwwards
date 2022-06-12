from django.shortcuts import render, redirect
from .forms import MyCreateUserForm
from django.contrib import messages
from base.models import Ratings, User, Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from cloudinary.forms import cl_init_js_callbacks

# Create your views here.

def home(request):
   posts = Post.objects.all()
   
   context = {'title':'Awwwords - Home', 'posts':posts}
   return render(request, 'home.html', context)
  
def loginPage(request):
   if request.user.is_authenticated:
     return redirect('home')
   if request.method == 'POST':
     email = request.POST['email'].lower()
     password = request.POST['password']
     print(email)
     print(password)
     try:
         user = User.objects.get(email=email)
     except:
         messages.error(request, 'User not exist.')
         
     user = authenticate(request, email=email, password=password)
     if user:
         login(request, user)
         
         return redirect('home')
     else:
         messages.error(request, 'Email or password incorrect.')
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
               login(request, user)
               return redirect('home')       
           else:
             messages.error(request, 'An error ocurred during registration.')
          
   return render(request, 'register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def profile(request, us):
   account = User.objects.get(username=us)
   posts = Post.objects.filter(user__username=us)
   context = {'title':'Awwwords - Profile', 'account':account, 'posts':posts}
   return render(request, 'profile.html', context)

@login_required(login_url='login')
def upload(request):
   context = {'title':'Awwwords - Upload'}
   if request.method == 'POST':
      image = request.FILES.get('image')
      title = request.POST.get('title')
      url = request.POST.get('url')
      feedback = request.POST.get('feedback')
      post = Post.objects.create(user=request.user, title=title, url=url, image=image, feedback=feedback)
      post.save()
      return redirect('home')
   return render(request, 'upload.html', context)

@login_required(login_url='login')
def post(request, pk):
   post = Post.objects.get(id=pk)
   if request.method == 'POST':
      print(request.POST)
      rate = int(request.POST.get('rate'))
      feedback = request.POST.get('feedback')
      print(request.POST)
      rating = Ratings.objects.create(user=request.user, post=post, stars=rate, body=feedback)
      rating.save()
      post.comments = post.comments + 1
      post.tota_rating = post.tota_rating + rate
      post.save()
      return redirect('post', pk=post.id)
   over_rall = round(post.tota_rating / post.comments)
   rating_info = post.ratings_set.all().order_by('-created')
   context = {'title':'Awwwords - Post', 'post':post, 'rating_info':rating_info, 'over_rall':over_rall}
   return render(request, 'post.html', context)


def searchResults(request):
   if request.method == 'POST':
        q = request.POST.get('q')
        print(q)
        posts = Post.objects.filter(Q(title__icontains=q))
        context = {'title':'Awwwords - Search', 'q':q, 'posts':posts}
        return render(request, 'search_result.html', context)
   
   context = {'title':'Awwwords - Search'}
   return render(request, 'search_result.html', context)