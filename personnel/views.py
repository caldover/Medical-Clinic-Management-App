from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.db import transaction
from .models import Personnel, Physician, Surgeon, Nurse
from localflavor.us.forms import USPhoneNumberField
from extra_views import CreateWithInlinesView, InlineFormSet
#from .forms import PhysicianFormSet
#from .forms import PhysicianForm
from django.core.urlresolvers import reverse
from django.shortcuts import render



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


class PersonnelCreate(CreateView):
    model = Personnel
    template_name = 'personnel/personnel_form.html'
    phone = USPhoneNumberField()
    fields = ['first_name', 'last_name', 'gender', 'address', 'phone', 'salary', 'ssn']
#
#     def form_valid(self, form):
#         # Get a new object based on the form
#         self.object = form.save(commit=False)
#         self.object.save()
#
#         # Use new object to assign to second model
#         physician_info = Physician(employee_no=self.object, )
#         physician_info.save()
#
#         return HttpResponseRedirect(self.get_absolute_url)

# class PersonnelPhysicianCreate(CreateView):
#     model = Personnel
#     template_name = 'personnel/personnel_form.html'
#     phone = USPhoneNumberField()
#     fields = ['first_name', 'last_name', 'gender', 'address', 'phone', 'salary', 'ssn']
#
#     def get_context_data(self, **kwargs):
#         data = super(PersonnelPhysicianCreate, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['physician'] = PhysicianFormSet(self.request.POST, instance=self.object)
#         else:
#             data['physician'] = PhysicianFormSet(instance=self.object)
#         return data
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         physician = context['physician']
#         with transaction.atomic():
#             self.object = form.save()
#
#             if physician.is_valid():
#                 physician.instance = self.object
#                 physician.save()
#         return super(PersonnelPhysicianCreate, self).form_valid(form)


# class PhysicianInline(InlineFormSet):
#     model = Physician
#     fields = '__all__'

# class PhysicianCreate(CreateWithInlinesView):
#     model = Personnel
#     inlines = [PhysicianInline]
#     fields = '__all__'
#     template_name = 'personnel/personnel_form.html'

# class PersonnelCreate(CreateView):
#     model = Personnel
#     template_name = 'personnel/personnel_form.html'
#     phone = USPhoneNumberField()
#     fields = ['first_name', 'last_name', 'gender', 'address', 'phone', 'salary', 'ssn']
#
# class PhysicianCreate(CreateView):
#     model = Physician
#     template_name = 'personnel/personnel_form.html'
#     fields = ['specialty']

# def physicianView(request):
#     if request.method == 'POST':
#         form = PhysicianForm(request.POST)
#         if form.is_valid():
#             first_name = request.POST.get('first_name', '')
#             last_name = request.POST.get('last_name', '')
#             gender = request.POST.get('gender', '')
#             address = request.POST.get('address', '')
#             phone = request.POST.get('phone', '')
#             salary = request.POST.get('salary', '')
#             ssn = request.POST.get('ssn', '')
#             specialty = request.POST.get('specialty', '')
#
#             personnel_obj = Personnel(first_name = first_name, last_name = last_name, gender = gender,
#                                      address = address, phone = phone, salary = salary, ssn = ssn)
#             personnel_obj.save()
#
#             physician_obj = Physician(employee_no_id = personnel_obj, specialty = specialty)
#             physician_obj.save()
#
#             return HttpResponseRedirect(reverse('personnel:index'))
#
#         else:
#            form = PhysicianForm()
#
#         return render(request, 'personnel/personnel_form.html', {'form': form})