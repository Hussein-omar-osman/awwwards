from django.shortcuts import render
from .forms import MyCreateUserForm
# Create your views here.

def home(request):
   return render(request, 'home.html')
  
def loginPage(request):
   return render(request, 'login.html')
  
def registerPage(request):
   form = MyCreateUserForm()
   context = {'form':form}
   return render(request, 'register.html', context)


def profile(request):
   return render(request, 'profile.html')

def upload(request):
   return render(request, 'upload.html')

def post(request):
   if request.method == 'POST':
      print(request.POST)
   return render(request, 'post.html')