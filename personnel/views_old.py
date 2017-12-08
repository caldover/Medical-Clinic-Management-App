from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from .models import Personnel

# Create your views here.

def index(request):
    all_personnel = Personnel.objects.all()

    # html = ''
    # for personnel in all_personnel:
    #     url = '/personnel/' + str(personnel.id) + '/'
    #     html += '<a href="' + url + '">' + personnel.first_name + ' ' + personnel.last_name  +'</a><br>'

    # template = loader.get_template('personnel/index.html')

    context = {
        'all_personnel': all_personnel,
    }

    # return HttpResponse(template.render(context, request))

    return render(request, 'personnel/index.html', context)

def detail(request, employee_no):
    # return HttpResponse("<h2>Details for Employee: " + str(employee_no) + "</h2>")

    try:
        personnel = Personnel.objects.get(pk=employee_no)
    except Personnel.DoesNotExist:
        raise Http404("Personnel does not exist")
    return render(request, 'personnel/detail.html', {'personnel': personnel})