from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse

def role_required(role):
    def check_role(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(check_role)

@login_required
@role_required('Admin')
def admin_view(request):
    return HttpResponse("Welcome Admin!")

@login_required
@role_required('Librarian')
def librarian_view(request):
    return HttpResponse("Welcome Librarian!")

@login_required
@role_required('Member')
def member_view(request):
    return HttpResponse("Welcome Member!")

