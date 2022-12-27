from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import CustomUserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.

def index(request):
  if  not request.user.is_authenticated: 
    return redirect("login/")
  return render(request, 'accounts/index.html')

def user_login(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        messages.info(request, f"Ypu are now logged")
        return render(request, 'landing/index.html')
      else:
        messages.error(request, "Invalid username or password")
    else:
      messages.error(request, "Invalud username or password")
  form = AuthenticationForm() 
  context = {}
  return render(request, 'registration/login.html', context={"login_form":form})

def sign_up(request):
  context = {}
  form = CustomUserCreationForm(request.POST or None)
  if request.method == "POST":
    if form.is_valid():
      user = form.save()
      login(request, user)
    return render(request, 'accounts/index.html')
  context['form'] = form
  return render(request, 'registration/sign_up.html', context)

def user_logout(request):
  logout(request)
  return render(request,'registration/logged_out.html')
