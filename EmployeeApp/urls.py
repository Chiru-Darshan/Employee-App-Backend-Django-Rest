from EmployeeApp import views
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^department$', views.departmentApi),
    re_path(r'^department/([0-9]+)$', views.departmentApi),
    re_path(r'^employee$', views.employeeApi),
    re_path(r'^employee/([0-9]+)$', views.employeeApi),
    re_path(r'^saveFile$', views.saveFile)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
