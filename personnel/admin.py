from django.contrib import admin
from .models import Personnel, Physician, Surgeon, Nurse, Shift, Schedule

# Register your models here.
admin.site.register(Personnel)
admin.site.register(Physician)
admin.site.register(Surgeon)
admin.site.register(Nurse)
admin.site.register(Shift)
admin.site.register(Schedule)