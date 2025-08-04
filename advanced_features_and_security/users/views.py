from django.shortcuts import render
from django.contrib.auth import get_user_model

def user_list(request):
    CustomUser = get_user_model()
    users = CustomUser.objects.all()
    return render(request, 'users/user_list.html', {'users': users})
