from django.urls import path
from . import views

urlpatterns = [
    path('libraries/', views.list_libraries, name='libraries'),
    path('books/', views.list_books, name='books'),
    path('admin-role/', views.admin_view, name='admin-role'),
    path('librarian-role/', views.librarian_view, name='librarian-role'),
    path('member-role/', views.member_view, name='member-role'),
]
