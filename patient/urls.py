from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView

app_name = 'patient'

urlpatterns = [
    # /patient/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /patients/add/
    url(r'add/$', views.PatientCreate.as_view(), name='patient-add'),
]