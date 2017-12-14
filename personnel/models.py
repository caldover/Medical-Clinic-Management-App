from django.db import models
from django.core.urlresolvers import reverse

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
    phone = models.CharField(max_length=12)
    salary = models.IntegerField()
    ssn = models.IntegerField()

    def get_absolute_url(self):
        return reverse('personnel:detail', kwargs={'pk': self.pk})

    def __str__(self):
         return self.first_name + ' ' + self.last_name


class PhysicianManager(models.Manager):
    def create_physician(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO `test_1`.`personnel_personnel` (`first_name`, `last_name`, `gender`, `address`, `phone`,
                 `salary`, `ssn`) 
	                VALUES ('Carl', 'Dio', 'M', '3 Street', 1234567892, 105000,545667456)
                """)
            cursor.execute("""
                SELECT *
                FROM `test_1`.`personnel_personnel` personnel
                WHERE personnel.id = LAST_INSERT_ID()
                """)

            result_list = []
            row = cursor.fetchone()
            result_list.append(row)

            cursor.execute("""
                INSERT INTO `test_1`.`personnel_physician`(`specialty`, `employee_no_id`)
                    VALUES('Cardiologist', LAST_INSERT_ID())
                """)
            cursor.execute("""
                SELECT physician.specialty
                FROM `test_1`.`personnel_physician` physician
                WHERE personnel.id = LAST_INSERT_ID()
                """)

            row = cursor.fetchone()
            result_list.append(row)

        return result_list


class Physician(models.Model):
    employee_no = models.OneToOneField(Personnel, on_delete=models.CASCADE, primary_key=True)
    specialty = models.CharField(max_length=50)

    objects = PhysicianManager()

    #def get_absolute_url(self):
    #    return reverse('personnel:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.employee_no)


class Surgeon(models.Model):
    employee_no = models.OneToOneField(Personnel, on_delete=models.CASCADE, primary_key=True)
    specialty = models.CharField(max_length=50)
    contract_type = models.CharField(max_length=20)
    #contract_length = models.DateField('contract_length', blank=True, null=True)
    #surgery_type_no = models.IntegerField()

    def __str__(self):
        return str(self.employee_no)


class Nurse(models.Model):
    employee_no = models.OneToOneField(Personnel, on_delete=models.CASCADE, primary_key=True)
    grade = models.CharField(max_length=1)  # A, B, C, D, E, F
    years_exp = models.IntegerField()

    def __str__(self):
        return str(self.employee_no)


class Shift(models.Model):
    date = models.DateField()
    employee_no = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    working_ind = models.BooleanField()

    class Meta:
        unique_together = ('date', 'employee_no')

    def __str__(self):
        return str(self.date)


class Schedule(models.Model):
    shift_no = models.OneToOneField(Shift, on_delete=models.CASCADE)
    block1 = models.BooleanField()
    block2 = models.BooleanField()
    block3 = models.BooleanField()
    block4 = models.BooleanField()
    block5 = models.BooleanField()
    block6 = models.BooleanField()
    block7 = models.BooleanField()
    block8 = models.BooleanField()