from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def check_role(user, role):
    return hasattr(user, 'userprofile') and user.userprofile.role == role

@user_passes_test(lambda u: check_role(u, 'Admin'))
def admin_view(request):
    return render(request, 'admin_page.html')

@user_passes_test(lambda u: check_role(u, 'Librarian'))
def librarian_view(request):
    return render(request, 'librarian_page.html')

@user_passes_test(lambda u: check_role(u, 'Member'))
def member_view(request):
    return render(request, 'member_page.html')
