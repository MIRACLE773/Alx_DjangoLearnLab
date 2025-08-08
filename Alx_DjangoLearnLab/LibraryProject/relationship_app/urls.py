from django.urls import path
from . import views

urlpatterns = [
    path('add-book/', views.add_book_view, name='add_book'),
    path('edit-book/<int:book_id>/', views.edit_book_view, name='edit_book'),
    path('delete-book/<int:book_id>/', views.delete_book_view, name='delete_book'),
]

