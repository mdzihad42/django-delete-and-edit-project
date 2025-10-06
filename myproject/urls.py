
from django.contrib import admin
from django.urls import path
from myproject.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('department/',departmentPage,name="department"),
    path('patient/',patientPage,name="patient"),
    path('doctor/',doctorPage,name="doctor"),
    path('apoint/',apPage,name="apoint"),
    path('delete/<int:id>',deleteOption,name="delete"),
    path('edit/<int:id>',editOption,name="edit"),
    path('patientDelete/<int:id>',patientDelete,name="patientDelete"),
    path('patientEdit/<int:id>',patientEdit,name="patientEdit"),
    path('apointDelete/<int:id>',apointDelete,name="apointDelete"),
    path('apointEdit/<int:id>',apointEdit,name="apointEdit"),
    path('departEdit/<int:id>',departEdit,name="departEdit"),
    path('departmentDelete/<int:id>',departmentDelete,name="departmentDelete")
]
