from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),  # this is now the root of the app
]
