from django.urls import path
from . import views

urlpatterns = [
    path('admin-role/', views.admin_view, name='admin-role'),
    path('librarian-role/', views.librarian_view, name='librarian-role'),
    path('member-role/', views.member_view, name='member-role'),
]
