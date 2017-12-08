from django.conf.urls import url
from . import views

app_name = 'personnel'

urlpatterns = [
    # /personnel/
    url(r'^$', views.index, name='index'),

    # /personnel/employee_no
    url(r'^(?P<employee_no>[0-9]+)/$', views.detail, name='detail'),
]
