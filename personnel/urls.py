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
    url(r'add/$', views.PersonnelCreate.as_view(), name='personnel-add'),

    # /personnel/add/
    #url(r'add/$', views.PersonnelPhysicianCreate.as_view(), name='personnel-add'),
    # url(r'add/$', views.PhysicianCreate.as_view(), name='personnel-add'),
    # url(r'add/$', views.PersonnelCreate.as_view(), name='personnel-add'),
    # url(r'add/$', views.physicianView, name='personnel-add'),
]
