from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Hello Admin! Welcome to your dashboard.")

@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Hello Librarian! Welcome to your dashboard.")

@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Hello Member! Welcome to your dashboard.")

