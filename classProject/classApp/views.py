from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book

# Create your views here.
def index(request):
    return HttpResponse("Hello Book World")

def addBook(request):
    book1 = Book(name="Halo", pageNumber=257, genre="action", publishDate="2018-07-17")
    book1.save()
    return HttpResponse("Added Book Bruh")

def allBook(request):
    bookList = Book.objects.all()
    for eachElement in bookList:
        print(eachElement.name)
    return HttpResponse(eachElement.name)
