from django.views import generic
from .models import Personnel, Physician, Surgeon, Nurse


class IndexView(generic.ListView):
    template_name = 'personnel/index.html'
    context_object_name = 'all_personnel'

    def get_queryset(self):
        return Personnel.objects.all()


class PhysiciansView(generic.ListView):
    template_name = 'personnel/physicians.html'
    context_object_name = 'all_physicians'

    def get_queryset(self):
        #return Physician.objects.all()
        #return Physician.objects.select_related('employee_no').values('employee_no_id')
        return Physician.objects.select_related('employee_no')


class SurgeonsView(generic.ListView):
    template_name = 'personnel/surgeons.html'
    context_object_name = 'all_surgeons'

    def get_queryset(self):
        return Surgeon.objects.select_related('employee_no')


class NursesView(generic.ListView):
    template_name = 'personnel/nurses.html'
    context_object_name = 'all_nurses'

    def get_queryset(self):
        return Nurse.objects.select_related('employee_no')


class DetailView(generic.DetailView):
    model = Personnel
    template_name = 'personnel/detail.html'

