from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Role-based access (optional but useful)
def check_role(role):
    def inner(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(inner)

@login_required
@check_role("Admin")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@login_required
@check_role("Librarian")
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@login_required
@check_role("Member")
def member_view(request):
    return render(request, "relationship_app/member_view.html")

# Permission-protected views
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
