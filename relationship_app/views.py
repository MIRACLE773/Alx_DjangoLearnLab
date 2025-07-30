<<<<<<< HEAD
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
=======
from django.http import HttpResponse
from .models import Library, Book
from django.contrib.auth.decorators import user_passes_test

def list_libraries(request):
    libraries = Library.objects.all()
    output = ', '.join([library.name for library in libraries])
    return HttpResponse(f"Libraries: {output}")

def list_books(request):
    books = Book.objects.all()
    output = ', '.join([book.title for book in books])
    return HttpResponse(f"Books: {output}")

>>>>>>> 3d6844a3686b4fb9f53fc556c1492935bba6b3f2

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

<<<<<<< HEAD
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
=======
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin!")

@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian!")

@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome, Member!")
>>>>>>> 3d6844a3686b4fb9f53fc556c1492935bba6b3f2
