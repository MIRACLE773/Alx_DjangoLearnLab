# relationship_app/urls.py
from django.urls import path
from .views import (
    home_view,
    list_books,
    LibraryDetailView,
    login_view,
    logout_view,
    register_view,
    admin_view,
    librarian_view,
    member_view,
)

urlpatterns = [
    path('', home_view, name='home'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

    # Role-based access URLs
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]

