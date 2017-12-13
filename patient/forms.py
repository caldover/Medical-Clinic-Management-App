from django import forms
from localflavor.us.forms import USPhoneNumberField



class PatientForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    gender = forms.CharField(max_length=1)  # M or F
    address = forms.CharField(max_length=100)
    phone = USPhoneNumberField()
    salary = forms.IntegerField()
    ssn = forms.IntegerField()
    blood_type = forms.CharField(max_length=2)