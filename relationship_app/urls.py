from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('admin-only/', views.admin_view, name='admin_view'),
    path('librarian-only/', views.librarian_view, name='librarian_view'),
    path('member-only/', views.member_view, name='member_view'),
=======
    path('admin-role/', views.admin_view, name='admin-role'),
    path('librarian-role/', views.librarian_view, name='librarian-role'),
    path('member-role/', views.member_view, name='member-role'),
>>>>>>> 3d6844a3686b4fb9f53fc556c1492935bba6b3f2
]
