from django.shortcuts import render
from .models import CustomUser

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'users/list.html', {'users': users})
