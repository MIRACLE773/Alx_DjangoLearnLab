from django.http import HttpResponse
from .models import Library, Book

def list_libraries(request):
    libraries = Library.objects.all()
    output = ', '.join([library.name for library in libraries])
    return HttpResponse(f"Libraries: {output}")

def list_books(request):
    books = Book.objects.all()
    output = ', '.join([book.title for book in books])
    return HttpResponse(f"Books: {output}")
