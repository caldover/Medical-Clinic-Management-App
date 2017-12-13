from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView

app_name = 'patient'

urlpatterns = [
    # /patient/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /patient/employee_no
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /patients/add/
    url(r'add/$', views.PatientCreate.as_view(), name='patient-add'),
]