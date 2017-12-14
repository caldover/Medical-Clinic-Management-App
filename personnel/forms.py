# from django.forms import ModelForm, inlineformset_factory
from django import forms
from localflavor.us.forms import USPhoneNumberField
from .models import Personnel, Physician, Shift, Schedule
import datetime

#
#
# class PersonnelForm(ModelForm):
#     class Meta:
#         model = Personnel
#         exclude = ()
#
#
# class PhysicianForm(ModelForm):
#     class Meta:
#         model = Physician
#         exclude = ()
#
#
# PhysicianFormSet = inlineformset_factory(Personnel, Physician, form=PhysicianForm, extra=1)

class PhysicianForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    gender = forms.CharField(max_length=1)  # M or F
    address = forms.CharField(max_length=100)
    phone = USPhoneNumberField()
    salary = forms.IntegerField()
    ssn = forms.IntegerField()
    specialty = forms.CharField(max_length=50)


class SurgeonForm(forms.Form):

    # def clean_date(self):
    #     contract_length = self.cleaned_data['contract_length']
    #     if contract_length < datetime.date.today():
    #         raise forms.ValidationError("Please enter a date that is not in the past.")
    #     return contract_length

    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    gender = forms.CharField(max_length=1)  # M or F
    address = forms.CharField(max_length=100)
    phone = USPhoneNumberField()
    salary = forms.IntegerField()
    ssn = forms.IntegerField()
    specialty = forms.CharField(max_length=50)
    contract_type = forms.CharField(max_length=50)
    # contract_length = forms.DateField(label='contract_length', initial=datetime.date.today, input_formats=['%Y-%m-%d', ])
    # surgery_type_no = ...


class NurseForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    gender = forms.CharField(max_length=1)  # M or F
    address = forms.CharField(max_length=100)
    phone = USPhoneNumberField()
    salary = forms.IntegerField()
    ssn = forms.IntegerField()
    grade = forms.CharField(max_length=1)
    years_exp = forms.IntegerField()


class ShiftForm(forms.Form):
    employee_no = forms.ModelChoiceField(label='Personnel Name', queryset=Personnel.objects.all())
    date = forms.DateField(label='Date', initial=datetime.date.today,
                                      input_formats=['%Y-%m-%d', ])


class PhysicianGetShiftForm(forms.Form):
    employee_no = forms.ModelChoiceField(label='Physician Name', queryset=Physician.objects.all())
    date = forms.ModelChoiceField(label='Available Dates', queryset=Shift.objects.all())

    def __init__(self, *args, **kwargs):
        employee_no_id = kwargs.pop('employee_no_id', None)
        super(PhysicianGetShiftForm, self).__init__(*args, **kwargs)

        if employee_no_id:
            self.fields['date'].queryset = Shift.objects.filter(employee_no_id=employee_no_id)

    #choices = [(i, i) for i in Schedule.get_all_field_names()]
    #block = forms.ChoiceField(label='Available Hours', choices=choices)

