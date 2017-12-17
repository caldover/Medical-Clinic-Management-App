from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.db import transaction
from .models import Personnel, Physician, Surgeon, Nurse, Shift, Schedule, TimeBlock
from localflavor.us.forms import USPhoneNumberField
from extra_views import CreateWithInlinesView, InlineFormSet
#from .forms import PhysicianFormSet
#from .forms import PhysicianForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from .forms import PhysicianForm, SurgeonForm, NurseForm, ShiftForm, PhysicianGetShiftForm, PhysicianSelectTimeForm, PhysicianGetDateForm
from . import values
import datetime



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

    #context_object_name = 'personnel_list'
    # def get_context_data(self, **kwargs):
    #     context = super(DetailView, self).get_context_data(**kwargs)
    #     context.update({
    #         'personnel_list': Physician.objects.all(),
    #         'personnel': Personnel.objects.all()
    #     })
    #     return context

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        try:
            context['physician'] = Physician.objects.get(employee_no_id=self.kwargs['pk'])
        except Physician.DoesNotExist:
            context['physician'] = None

        try:
            context['surgeon'] = Surgeon.objects.get(employee_no_id=self.kwargs['pk'])
        except Surgeon.DoesNotExist:
            context['surgeon'] = None

        try:
            context['nurse'] = Nurse.objects.get(employee_no_id=self.kwargs['pk'])
        except Nurse.DoesNotExist:
            context['nurse'] = None

        return context

    def get_queryset(self):
        return Personnel.objects.all()


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

def get_physician_info(request):
    if request.method == 'POST':
        form = PhysicianForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            salary = form.cleaned_data['salary']
            ssn = form.cleaned_data['ssn']
            specialty = form.cleaned_data['specialty']

            personnel = Personnel(first_name=first_name, last_name=last_name, gender=gender, address=address,
                                  phone=phone, salary=salary, ssn=ssn)
            personnel.save()

            physician = Physician(employee_no_id=personnel.id, specialty=specialty)
            physician.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('personnel:index'))
        else:
            print(form.errors)

    else:
        form = PhysicianForm()

    return render(request, 'personnel/physician_form.html', {'form': form})


def get_surgeon_info(request):
    if request.method == 'POST':
        form = SurgeonForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            salary = form.cleaned_data['salary']
            ssn = form.cleaned_data['ssn']
            specialty = form.cleaned_data['specialty']
            contract_type = form.cleaned_data['contract_type']
            # contract_length = form.cleaned_data['contract_type']

            personnel = Personnel(first_name=first_name, last_name=last_name, gender=gender, address=address,
                                  phone=phone, salary=salary, ssn=ssn)
            personnel.save()

            surgeon = Surgeon(employee_no_id=personnel.id, specialty=specialty, contract_type=contract_type, )
            surgeon.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('personnel:index'))
        else:
            print(form.errors)

    else:
        form = SurgeonForm()

    return render(request, 'personnel/surgeon_form.html', {'form': form})


def get_nurse_info(request):
    if request.method == 'POST':
        form = NurseForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            salary = form.cleaned_data['salary']
            ssn = form.cleaned_data['ssn']
            grade = form.cleaned_data['grade']
            years_exp = form.cleaned_data['years_exp']

            personnel = Personnel(first_name=first_name, last_name=last_name, gender=gender, address=address,
                                  phone=phone, salary=salary, ssn=ssn)
            personnel.save()

            nurse = Nurse(employee_no_id=personnel.id, grade=grade, years_exp=years_exp)
            nurse.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('personnel:index'))
        else:
            print(form.errors)

    else:
        form = NurseForm()

    return render(request, 'personnel/nurse_form.html', {'form': form})


def get_shift_info(request):
    if request.method == 'POST':
        form = ShiftForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            employee_no = form.cleaned_data['employee_no']
            date = form.cleaned_data['date']

            shift = Shift(employee_no_id=employee_no.pk , date=date, working_ind=True)
            shift.save()

            schedule = Schedule(shift_no_id=shift.id , block1=False, block2=False, block3=False,
                                block4=False, block5=False, block6=False, block7=False, block8=False)
            schedule.save()

            time_block1 = TimeBlock(shift_no_id=shift.id, time=' 9am - 10am' , attending=False)
            time_block1.save()

            time_block2 = TimeBlock(shift_no_id=shift.id, time='10am - 11am', attending=False)
            time_block2.save()

            time_block3 = TimeBlock(shift_no_id=shift.id, time='11am - 12pm', attending=False)
            time_block3.save()

            time_block4 = TimeBlock(shift_no_id=shift.id, time='12pm -  1pm', attending=False)
            time_block4.save()

            time_block5 = TimeBlock(shift_no_id=shift.id, time=' 1pm -  2pm', attending=False)
            time_block5.save()

            time_block6 = TimeBlock(shift_no_id=shift.id, time=' 2pm -  3pm', attending=False)
            time_block6.save()

            time_block7 = TimeBlock(shift_no_id=shift.id, time=' 3pm -  4pm', attending=False)
            time_block7.save()

            time_block8 = TimeBlock(shift_no_id=shift.id, time=' 4pm -  5pm', attending=False)
            time_block8.save()


            # redirect to a new URL:
            return HttpResponseRedirect(reverse('personnel:index'))
        else:
            print(form.errors)

    else:
        form = ShiftForm()

    return render(request, 'personnel/shift_form.html', {'form': form})


def get_physician_shift_info(request):
    if request.method == 'POST':
        form = PhysicianGetShiftForm(request.POST)
        if form.is_valid():
            employee_no = form.cleaned_data['employee_no']
            values.current_physician = employee_no.pk
            # form = PhysicianGetDateForm(request.POST, request=values.current_physician)
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('personnel:physician_dates', args=[values.current_physician]))
        else:
            print(form.errors)

    else:
        form = PhysicianGetShiftForm()

    return render(request, 'personnel/get_physician_shift_form.html', {'form': form})


# class DatesDetailView(generic.DetailView):
#     model = Personnel
#     template_name = 'personnel/shift_dates.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(DatesDetailView, self).get_context_data(**kwargs)
#         try:
#             context['all_dates'] = Shift.objects.filter(employee_no_id=self.kwargs['pk'])
#         except Shift.DoesNotExist:
#             context['all_dates'] = None
#
#         return context
#
#     def get_queryset(self):
#         return Personnel.objects.all()


def get_physician_date(request, pk):
    if request.method == 'POST':
        #form = PhysicianGetDateForm(request.POST, request=values.current_physician)
        values.current_physician = pk
        form = PhysicianGetDateForm(request.POST, request=pk)
        print(values.current_physician)
        print(pk)
        if form.is_valid():
            date_obj = form.cleaned_data['date']
            values.current_date = date_obj.date.strftime('%Y-%m-%d')

            shift = Shift.objects.get(date=values.current_date, employee_no_id=values.current_physician)
            #shift = Shift.objects.get(date=values.current_date, employee_no_id=pk)
            values.current_shift = shift.pk

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('personnel:physician_avail', args=[values.current_physician, values.current_date]))
        else:
            print(form.errors)

    else:
        print(values.current_physician)
        print(pk)
        form = PhysicianGetDateForm(request.POST, request=pk)

    return render(request, 'personnel/physician_dates.html', {'form': form})



class AvailView(generic.DetailView):
    model = Shift
    template_name = 'personnel/availability.html'

    def get_object(self):

        obj = get_object_or_404(
            self.model,
            employee_no_id=self.kwargs['employee_no_id'],
            #pub_date__date=self.kwargs['date'])
            date=self.kwargs['date'])

        return obj

    def get_context_data(self, **kwargs):
        context = super(AvailView, self).get_context_data(**kwargs)
        try:
            #context['schedule'] = Schedule.objects.get(shift_no_id=self.kwargs['id'])
            context['schedule'] = Schedule.objects.all()
        except Schedule.DoesNotExist:
            context['schedule'] = None

        return context

    def get_queryset(self):
        return Shift.objects.all()


def get_appointment_selection(request, employee_no_id, date):
    if request.method == 'POST':
        values.current_physician = employee_no_id
        values.current_date = date
        shift = Shift.objects.get(date=date, employee_no_id=employee_no_id)
        form = PhysicianSelectTimeForm(request.POST, request=shift.pk)
        #form = PhysicianSelectTimeForm(request.POST)
        if form.is_valid():
            time = form.cleaned_data['time']
            time.attending = True
            time.save()

            #shift = Shift.objects.get(date=date, employee_no_id=employee_no_id)
            # values.current_shift = shift
            #schedule = Schedule.objects.get(shift_no_id=values.current_shift)
            #schedule.block = True
            #schedule.save()

            time_block = TimeBlock.objects.get(shift_no_id=shift.pk)

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('personnel:index'))
        else:
            print(form.errors)
    else:
        form = PhysicianSelectTimeForm()
    return render(request, 'personnel/physician_times.html', {'form': form})