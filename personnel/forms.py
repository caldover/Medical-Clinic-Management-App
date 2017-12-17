# from django.forms import ModelForm, inlineformset_factory
from django import forms
from localflavor.us.forms import USPhoneNumberField
from .models import Personnel, Physician, Shift, Schedule, TimeBlock
from . import views
import datetime
from . import values
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


class PhysicianGetDateForm(forms.Form):
    #date = forms.ModelChoiceField(label='Date', queryset=Shift.objects.filter(employee_no_id=values.current_physician))
    # date = forms.ModelChoiceField(label='Date', queryset=Shift.objects.filter(employee_no_id=2))

    date = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request',None)

        # if not 'queryset' in kwargs:
        #     kwargs['queryset'] = Shift.objects.filter(employee_no_id=values.current_physician)
        # return super(PhysicianGetDateForm,self).__init__(*args,**kwargs)

        super(PhysicianGetDateForm, self).__init__(*args, **kwargs)
        self.fields['date'].queryset = Shift.objects.filter(employee_no_id=request)

        #super(PhysicianGetDateForm,self).__init__(*args,**kwargs)
            #self.fields['date'].choices = [x.date for x in Shift.objects.filter(employee_no_id=values.current_physician)]
        # self.fields['date'].choices = zip(
        #     [Shift.objects.filter(employee_no_id=values.current_physician)], [Shift.objects.filter(employee_no_id=values.current_physician)]
        # )



class PhysicianSelectTimeForm(forms.Form):
    # block_choices = []

    # block1 = Schedule.objects.only("block1")
    # if not block1:
    #     block_choices.append(('block1', ' 9am - 10am'))
    #
    # block2 = Schedule.objects.only("block2")
    # if not block2:
    #     block_choices.append(('block2', '10am - 11am'))
    #
    # block3 = Schedule.objects.only("block3")
    # if not block3:
    #     block_choices.append(('block3', '11am - 12pm'))
    #
    # block4 = Schedule.objects.only("block4")
    # if not block4:
    #     block_choices.append(('block4', '12pm -  1pm'))
    #
    # block5 = Schedule.objects.only("block5")
    # if not block5:
    #     block_choices.append(('block5', ' 1pm -  2pm'))
    #
    # block6 = Schedule.objects.only("block6")
    # if not block6:
    #     block_choices.append(('block6', ' 2pm -  3pm'))
    #
    # block7 = Schedule.objects.only("block7")
    # if not block7:
    #     block_choices.append(('block7', ' 3pm -  4pm'))
    #
    # block8 = Schedule.objects.only("block8")
    # if not block8:
    #     block_choices.append(('block8', ' 4pm -  5pm'))
    #
    #
    # block = forms.ChoiceField(choices=block_choices)

    #time = forms.ModelChoiceField(label='Time', queryset=TimeBlock.objects.filter(shift_no_id=values.current_shift))


    time = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)

        # if not 'queryset' in kwargs:
        #     kwargs['queryset'] = Shift.objects.filter(employee_no_id=values.current_physician)
        # return super(PhysicianGetDateForm,self).__init__(*args,**kwargs)

        super(PhysicianSelectTimeForm, self).__init__(*args, **kwargs)
        self.fields['time'].queryset = TimeBlock.objects.filter(shift_no_id=request)


