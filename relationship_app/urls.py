from django.urls import path
from . import views

urlpatterns = [
    path('libraries/', views.list_libraries, name='libraries'),
    path('books/', views.list_books, name='books'),
]
