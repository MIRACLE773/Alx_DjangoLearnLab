from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from .models import Book
from .forms import BookForm  
from django.http import HttpResponse

@permission_required('relationship_app.canaddbook')
def add_book_view(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # redirect to your book list view
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.canchangebook')
def edit_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

@permission_required('relationship_app.candeletebook')
def delete_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book_confirm.html', {'book': book})

@login_required
def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

def admin_view(request):
    return HttpResponse("Admin view placeholder")

