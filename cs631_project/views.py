from django.http import HttpResponse
from django.views.generic import TemplateView

# def home(request):
#     return HttpResponse("<h1>Welcome to the Newark Medical Associates Management System</h1>")


class Home(TemplateView):
    template_name = 'cs631_project/home.html'