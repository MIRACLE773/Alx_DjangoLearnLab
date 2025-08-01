from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from .models import UserProfile

def role_required(role_name):
    def check_role(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role_name
    return user_passes_test(check_role)

@login_required
@role_required('Admin')
def admin_view(request):
    return render(request, 'admin_view.html')

@login_required
@role_required('Librarian')
def librarian_view(request):
    return render(request, 'librarian_view.html')

@login_required
@role_required('Member')
def member_view(request):
    return render(request, 'member_view.html')


