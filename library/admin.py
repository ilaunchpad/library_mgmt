from django.contrib import admin

from .models import Book
admin.site.register(Book)

from .models import Checkout
admin.site.register(Checkout)
# Register your models here.
