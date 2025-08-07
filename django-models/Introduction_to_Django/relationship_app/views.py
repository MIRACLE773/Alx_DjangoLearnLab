from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from .models import UserProfile

def check_role(role):
    def test(user):
        if not user.is_authenticated:
            return False
        try:
            return user.userprofile.role == role
        except UserProfile.DoesNotExist:
            return False
    return test

@login_required
def home_view(request):
    # Home view accessible to any logged-in user
    try:
        role = request.user.userprofile.role
    except UserProfile.DoesNotExist:
        role = None
    return render(request, 'home.html', {'role': role})

@login_required
@user_passes_test(check_role('Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(check_role('Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
