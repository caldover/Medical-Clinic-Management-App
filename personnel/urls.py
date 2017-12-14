from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView

app_name = 'personnel'

urlpatterns = [
    # /personnel/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /personnel/physicians
    url(r'physicians/$', views.PhysiciansView.as_view(), name='physicians'),

    # /personnel/surgeons
    url(r'surgeons/$', views.SurgeonsView.as_view(), name='surgeons'),

    # /personnel/nurses
    url(r'nurses/$', views.NursesView.as_view(), name='nurses'),

    # /personnel/employee_no
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /personnel/physicians/employee_no
    # url(r'physicians/^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'physicians/^(?P<pk>[0-9]+)/$', RedirectView.as_view(pattern_name='detail', permanent=False), name='physician_detail'),

    # /personnel/add/
    #url(r'add/$', views.PersonnelCreate.as_view(), name='personnel-add'),

    # /personnel/add/
    #url(r'add/$', views.PersonnelPhysicianCreate.as_view(), name='personnel-add'),
    # url(r'add/$', views.PhysicianCreate.as_view(), name='personnel-add'),
    # url(r'add/$', views.PersonnelCreate.as_view(), name='personnel-add'),
    # url(r'add/$', views.physicianView, name='personnel-add'),

    # /personnel/shift/
    url(r'shift/$', views.get_shift_info, name='shift-add'),

    # /personnel/physicians/add/
    url(r'physicians/add/$', views.get_physician_info, name='physician-add'),

    # /personnel/physicians/availability/
    #url(r'physicians/availability/$', views.get_physician_shift_info, name='get-physician-avail'),

    # /personnel/availability/employee_no/date/
    url(r'availability/^(?P<employee_no_id>[0-9]+)/^(?P<date>\d{4}-\d{2}-\d{2})/$', views.AvailView.as_view(), name='physician_avail2'),

    # /personnel/physicians/availability/employee_no/date/
    url(r'physicians/availability/^(?P<employee_no_id>[0-9]+)/^(?P<date>\d{4}-\d{2}-\d{2})/$', views.AvailView.as_view(), name='physician_avail'),

    # /personnel/surgeons/add/
    url(r'surgeons/add/$', views.get_surgeon_info, name='surgeon-add'),

    # /personnel/nurses/add/
    url(r'nurses/add/$', views.get_nurse_info, name='nurse-add'),

]
