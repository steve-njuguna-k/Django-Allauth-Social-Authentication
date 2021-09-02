from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def Login(request):
    return render(request, 'Login.html')

def Register(request):
    return render(request, 'Register.html')

def Home(request):
    return render(request, 'Home.html')

def Logout(request):
    logout(request)
    return redirect('Login')