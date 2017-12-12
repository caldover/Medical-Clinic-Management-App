from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView

app_name = 'personnel'

urlpatterns = [
    # /personnel/
    url(r'personnel/^$', views.IndexView.as_view(), name='index'),

    # /personnel/physicians
    url(r'personnel/physicians/$', views.PhysiciansView.as_view(), name='physicians'),

    # /personnel/surgeons
    url(r'personnel/surgeons/$', views.SurgeonsView.as_view(), name='surgeons'),

    # /personnel/nurses
    url(r'personnel/nurses/$', views.NursesView.as_view(), name='nurses'),

    # /personnel/employee_no
    url(r'personnel/^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /personnel/physicians/employee_no
    # url(r'physicians/^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'personnel/physicians/^(?P<pk>[0-9]+)/$', RedirectView.as_view(pattern_name='detail', permanent=False), name='physician_detail'),

    # /personnel/add/
    #url(r'add/$', views.PersonnelCreate.as_view(), name='personnel-add'),

    # /personnel/add/
    #url(r'add/$', views.PersonnelPhysicianCreate.as_view(), name='personnel-add'),
    # url(r'add/$', views.PhysicianCreate.as_view(), name='personnel-add'),
    # url(r'add/$', views.PersonnelCreate.as_view(), name='personnel-add'),
    # url(r'add/$', views.physicianView, name='personnel-add'),

    # /personnel/physician/add/
    url(r'personnel/physicians/add/$', views.get_physician_info, name='physician-add'),

    # /physicians/employee_no
    url(r'physicians/add/$', RedirectView.as_view(pattern_name='index', permanent=False), name='physician-add-redir'),

]
