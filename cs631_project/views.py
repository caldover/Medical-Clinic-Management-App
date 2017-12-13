from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Newark Medical Associates Management System</h1>")