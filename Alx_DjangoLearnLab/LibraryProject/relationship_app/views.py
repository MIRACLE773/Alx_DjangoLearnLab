from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

def check_role(role):
    def inner(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(inner)

@login_required
@check_role("Admin")
def admin_view(request):
    return render(request, "admin_view.html")

@login_required
@check_role("Librarian")
def librarian_view(request):
    return render(request, "librarian_view.html")

@login_required
@check_role("Member")
def member_view(request):
    return render(request, "member_view.html")



