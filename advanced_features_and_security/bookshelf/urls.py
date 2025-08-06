from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user-list'),  # or whatever view you are using
]
