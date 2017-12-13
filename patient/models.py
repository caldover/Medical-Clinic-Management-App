from django.db import models
from django.core.urlresolvers import reverse


class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1) # M or F
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    ssn = models.IntegerField()
    blood_type = models.CharField(max_length=3)

    def get_absolute_url(self):
        return reverse('patient:detail', kwargs={'pk': self.pk})

    def __str__(self):
         return self.first_name + ' ' + self.last_name