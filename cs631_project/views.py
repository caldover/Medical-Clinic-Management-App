from django.http import HttpResponse
from django.views import generic

# def home(request):
#     return HttpResponse("<h1>Welcome to the Newark Medical Associates Management System</h1>")


class home(generic.ListView):
    template_name = 'cs631_project/home.html'