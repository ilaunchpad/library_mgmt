from django.shortcuts import render
from .models import Book
from rest_framework import generics
from .serializers import BookSerializer

from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views import generic
from django.template import loader
from .models import Book
# Create your views here.
import datetime
import json

def index(request):
  latest_book_list = Book.objects.all()
  print('lates_book_list:', latest_book_list)
  template = loader.get_template('library/index.html')
  print('template ', template)
  context = {
      'latest_book_list': latest_book_list,
      }
  return HttpResponse(template.render(context, request))

#def books(request):
 # return HttpResponse("This is a book page.")


###just do get books for now
@api_view(['GET'])
def books(request):
  print('request', request)
  if request.method=='GET':
    books = Book.objects.all()
    books_serialized = BookSerializer(books, many=True)
    print('books', books_serialized)
    template = loader.get_template('library/index.html')
    context = {
        'latest_book_list': books_serialized,
        }
    print('context ', context)
    return render(request, 'library/books.html',context)
    #return Response(template.render(books, request), safe=False)
    #return HttpResponse(books_serialized)

class BookView(generic.ListView):
  template_name = 'library/booklist.html'
  context_object_name = 'all_book_list'

