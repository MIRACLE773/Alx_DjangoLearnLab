from django.shortcuts import render
from django.contrib.auth import get_user_model

def user_list(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'users/list.html', {'users': users})
