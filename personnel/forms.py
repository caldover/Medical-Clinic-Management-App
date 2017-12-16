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
    #date = forms.ModelChoiceField(label='Available Dates', queryset=Shift.objects.all())

class PhysicianSelectTimeForm(forms.Form):
    block_choices = []

    block1 = Schedule.objects.only("block1")
    if block1:
        block_choices.append(block1)

    block2 = Schedule.objects.only("block2")
    if block2:
        block_choices.append(block2)

    block3 = Schedule.objects.only("block3")
    if block3:
        block_choices.append(block3)

    block4 = Schedule.objects.only("block4")
    if block4:
        block_choices.append(block4)

    block5 = Schedule.objects.only("block5")
    if block5:
        block_choices.append(block5)

    block6 = Schedule.objects.only("block6")
    if block6:
        block_choices.append(block6)

    block7 = Schedule.objects.only("block7")
    if block7:
        block_choices.append(block7)

    block8 = Schedule.objects.only("block8")
    if block8:
        block_choices.append(block8)

    block = forms.ChoiceField(choices=block_choices, widget=forms.RadioSelect)


