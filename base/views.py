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