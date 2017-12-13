from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.db import transaction
from .models import Patient
from localflavor.us.forms import USPhoneNumberField
from extra_views import CreateWithInlinesView, InlineFormSet
#from .forms import PhysicianFormSet
#from .forms import PhysicianForm
from django.core.urlresolvers import reverse
from django.shortcuts import render


class IndexView(generic.ListView):
    template_name = 'patient/index.html'
    context_object_name = 'all_patients'

    def get_queryset(self):
        return Patient.objects.all()


class PatientCreate(CreateView):
    model = Patient
    template_name = 'patient/patient_form.html'
    phone = USPhoneNumberField()
    fields = ['first_name', 'last_name', 'gender', 'address', 'phone', 'salary', 'ssn', 'blood_type']