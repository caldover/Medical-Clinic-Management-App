from django.db import models

# Create your models here.

'''
When creating new models, remember to do the following:
1. include app in settings.py --> INSTALLED_APPS
2. python manage.py makemigrations (app name)
3. python manage.py migrate
'''


class Personnel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1) # M or F
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    salary = models.IntegerField()
    ssn = models.IntegerField()

    def __str__(self):
         return self.first_name + ' ' + self.last_name


class Physician(models.Model):
    employee_no = models.OneToOneField(Personnel, on_delete=models.CASCADE, primary_key=True)
    specialty = models.CharField(max_length=50)

    def __str__(self):
        return str(self.employee_no)


class Surgeon(models.Model):
    employee_no = models.OneToOneField(Personnel, on_delete=models.CASCADE, primary_key=True)
    specialty = models.CharField(max_length=50)
    contract_type = models.CharField(max_length=20)
    contract_length = models.DateField()
    surgery_type_no = models.IntegerField()

    def __str__(self):
        return str(self.employee_no)


class Nurse(models.Model):
    employee_no = models.OneToOneField(Personnel, on_delete=models.CASCADE, primary_key=True)
    grade = models.CharField(max_length=1)  # A, B, C, D, E, F
    years_exp = models.IntegerField()

    def __str__(self):
        return str(self.employee_no)