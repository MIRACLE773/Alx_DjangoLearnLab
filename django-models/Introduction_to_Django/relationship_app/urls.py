from django.urls import path
from . import views  # you already have this

urlpatterns = [
    path('', views.home_view, name='home'),  
    path('admin-role/', views.admin_view, name='admin_view'),
    path('librarian-role/', views.librarian_view, name='librarian_view'),
    path('member-role/', views.member_view, name='member_view'),
]
