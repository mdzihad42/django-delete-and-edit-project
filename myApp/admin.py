from django.contrib import admin
from myApp.models import*
admin.site.register(departmentModel)
admin.site.register(doctorModel)
admin.site.register(patientModel)
admin.site.register(appointmentModel)
