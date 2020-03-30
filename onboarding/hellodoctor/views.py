from django.shortcuts import HttpResponse


# Create your views here.
def on_login(request):
    return HttpResponse("<h1>Hi</h1>")
