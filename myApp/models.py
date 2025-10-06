from django.db import models
class departmentModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    location=models.CharField(max_length=100,null=True)
    
    
    def __str__(self):
        
        return f"{self.name}"
class doctorModel(models.Model):
    select_sp=[
        ("Neurologist","Neurologist"),
        ("Psychiatrist","Psychiatrist"),
        ("Pathologist","Pathologist")
    ]
    name=models.CharField(max_length=100,null=True)
    specialization=models.CharField(choices=select_sp, max_length=100, null=True)
    phone=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=30,unique=True,null=True)
    department=models.ForeignKey(departmentModel, on_delete=models.CASCADE,null=True,related_name="doctor_dept")
    
    def __str__(self):
        return f"{self.name}"
    
    
class patientModel(models.Model):
    gender=[
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other")
    ]
    name=models.CharField(max_length=100,null=True)
    age=models.IntegerField()
    gender=models.CharField(choices=gender,max_length=20,null=True)
    phone=models.CharField(max_length=20, null=True)
    address=models.CharField(max_length=100,null=True)
    doctor=models.ForeignKey(doctorModel,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.name}"
    
class appointmentModel(models.Model):
    status_nm=[
        (" Pending","Pending"),
        ("Completed","Completed"),
        ("Cancelled","Cancelled")
    ]
    patient=models.ForeignKey(patientModel,on_delete=models.CASCADE,null=True)
    doctor=models.ForeignKey(doctorModel,on_delete=models.CASCADE,null=True)
    appointment_date=models.DateField()
    status=models.CharField(choices=status_nm,max_length=100,null=True,default="Pending")
    
    def __str__(self):
        return f"{self.patient}"