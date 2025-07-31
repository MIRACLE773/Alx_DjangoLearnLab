from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import UserProfile


@login_required
@user_passes_test(lambda u: u.userprofile.role == 'Admin')
def admin_view(request):
    return HttpResponse("Welcome Admin!")


@login_required
@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
def librarian_view(request):
    return HttpResponse("Welcome Librarian!")


@login_required
@user_passes_test(lambda u: u.userprofile.role == 'Member')
def member_view(request):
    return HttpResponse("Welcome Member!")
