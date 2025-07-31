from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse

# Decorators
def check_role(role):
    def inner_check(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(inner_check)

# Views
@login_required
@check_role('Admin')
def admin_view(request):
    return HttpResponse("Welcome Admin!")

@login_required
@check_role('Librarian')
def librarian_view(request):
    return HttpResponse("Welcome Librarian!")

@login_required
@check_role('Member')
def member_view(request):
    return HttpResponse("Welcome Member!")
