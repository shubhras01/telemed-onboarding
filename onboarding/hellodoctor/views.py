from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView


# Create your views here.
@login_required(login_url='/login/')
def on_login(request):
    return HttpResponse("<h1>Hello World</h1>")


class LoginAfterPasswordChangeView(PasswordChangeView):
    success_url = '/on_login/'
