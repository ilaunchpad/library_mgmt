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
from checkout.models import Checkout
from accounts.models import User
from library.models import Book
from library.serializers import BookSerializer
# Create your views here.

def index(request):
  if  not request.user.is_authenticated: 
    return redirect("login/")
  return render(request, 'accounts/index.html')

def user_profile(request):
  if request.method =="GET":
    if request.user.is_authenticated:
      cked_items = Checkout.objects.filter(userid=request.user.id)
      bl = []
      for items in cked_items:
        bl.append(items.bookid)
      books_serialized = BookSerializer(bl, many=True)   
      print(books_serialized)
      return render(request, 'accounts/profile_tbl.html', {'latest_book_list':books_serialized})

  if request.method =="POST":
    if request.user.is_authenticated:
      id_list = request.POST.getlist('boxes')
      print('id_list', id_list)
      if len(id_list) >  0:
        all_cked_items = Checkout.objects.filter(userid=request.user.id)
        cmn_items =[item for id in id_list for item in all_cked_items if item.bookid.id == int(id)]
        print('cmn_items',cmn_items)
        for item  in cmn_items:
          record = Checkout.objects.get(id=item.id)
          print('record', record)
          record.delete()
        for bid in id_list:
          book_record = Book.objects.get(id=int(bid))
          if not book_record.available:
            book_record.available=True
            book_record.save()
      cked_items_updated = Checkout.objects.filter(userid=request.user.id)    
      bl = []
      for items in cked_items_updated:
         bl.append(items.bookid)
      books_serialized = BookSerializer(bl, many=True)   
      print(books_serialized)
      return render(request, 'accounts/profile_tbl.html', {'latest_book_list':books_serialized})
  return HttpResponse("User is not logged in to show profile")

def user_login(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        ##messages.info(request, f"You are now logged")
        return render(request, 'landing/index.html')
      else:
        messages.error(request, "Invalid username or password")
    else:
      messages.error(request, "Invalid username or password")
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
    return render(request, 'landing/index.html')
  context['form'] = form
  return render(request, 'registration/sign_up.html', context)

def user_logout(request):
  logout(request)
  return render(request,'registration/logged_out.html')
