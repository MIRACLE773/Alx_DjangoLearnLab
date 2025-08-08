from django.urls import path
from . import views

urlpatterns = [
    path('admin-role/', views.admin_view, name='admin_view'),
    path('books/', views.book_list_view, name='book_list'),  
    path('add-book/', views.add_book_view, name='add_book'), 
    path('edit-book/<int:book_id>/', views.edit_book_view, name='edit_book'),      
    path('delete-book/<int:book_id>/', views.delete_book_view, name='delete_book'),
]

