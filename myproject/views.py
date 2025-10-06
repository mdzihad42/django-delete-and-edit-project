from django.shortcuts import render , redirect
from myApp.models import*

def doctorPage(request):
    if request.method=="POST":
        name=request.POST.get("name")
        specialization=request.POST.get("specialization")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        department=request.POST.get("department")
        dept_nm=departmentModel.objects.get(id=department)
        doctorModel.objects.create(
            name=name,
            specialization=specialization,
            phone=phone,
            email=email,
            department=dept_nm
        )
    name=doctorModel.objects.values_list("name",flat=True).distinct()
    select_name=request.GET.get("name")
    doctor=doctorModel.objects.all()
    if select_name:
        department=departmentModel.objects.get(name = select_name)
        doctor=doctorModel.objects.filter(department=department)
    else:
        doctor=doctorModel.objects.all()
    dept_data=departmentModel.objects.all()
    context={
        "dept_data":dept_data,
        "doctor":doctor,
        "name":name,
        "select_name":select_name
    }
    return render(request,"doctor.html",context)
def patientPage(request):
    if request.method =="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        phone=request.POST.get("phone")
        address=request.POST.get("address")
        doctor=request.POST.get("doctor")
        
        doctor_d=doctorModel.objects.get(id=doctor)
        patientModel.objects.create(
            name=name,
            age=age,
            gender=gender,
            phone=phone,
            address=address,
            doctor=doctor_d
        )
    name=patientModel.objects.values_list("name",flat=True).distinct()
    select_name=request.GET.get("name")
    if select_name:
        patient=patientModel.objects.filter(name=select_name)
    else:
        patient=patientModel.objects.all()
        
    doctor_data=doctorModel.objects.all()
    # patient=patientModel.objects.all()
    context={
        "doctor_data":doctor_data,
        "patient":patient,
        "name":name,
        "select_name":select_name
    }
    return render(request,"patient.html",context)


def apPage(request):
    if request.method=="POST":
        patient=request.POST.get("patient")
        doctor=request.POST.get("doctor")
        appointment_date=request.POST.get("appointment_date")
        status=request.POST.get("status")
        
        patient_p=patientModel.objects.get(id=patient)
        doctor_dm=doctorModel.objects.get(id=doctor)
        
        data=appointmentModel(
            patient=patient_p,
            doctor=doctor_dm,
            appointment_date=appointment_date,
            status=status
        )
        
        data.save()
    patient_data=patientModel.objects.all()
    doctor_data=doctorModel.objects.all()
    
    
    apoint=appointmentModel.objects.all()
    context={
        "patient_data":patient_data,
        "doctor_data":doctor_data,
        "apoint":apoint
    }
    return render(request,"apoint.html",context)
def deleteOption(request,id):
    delete_data=doctorModel.objects.get(id=id)
    delete_data.delete()
    return redirect("doctor")
def editOption(request,id):
    dept_data=departmentModel.objects.all()
    doctor=doctorModel.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("name")
        specialization=request.POST.get("specialization")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        department=request.POST.get("department")
        
        dept_nm=departmentModel.objects.get(id=department)
    
        doctorModel(
            id=id,
            name=name,
            specialization=specialization,
            phone=phone,
            email=email,
            department=dept_nm
        ).save()
        return redirect("doctor")
    context={
            "dept_data":dept_data,
            "doctor":doctor
        }
    return render(request,"doctorPage.html",context)
def patientDelete(request,id):
    delete_data=patientModel.objects.get(id=id)
    delete_data.delete()
    return redirect("patient")
def patientEdit(request,id):
    doctor_data=doctorModel.objects.all()
    patient=patientModel.objects.get(id=id)
    if request.method =="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        phone=request.POST.get("phone")
        address=request.POST.get("address")
        doctor=request.POST.get("doctor")
        
        doctor_d=doctorModel.objects.get(id=doctor)
        patientModel(
            id=id,
            name=name,
            age=age,
            gender=gender,
            phone=phone,
            address=address,
            doctor=doctor_d
        ).save()
        
        return redirect("patient")
    context={
        "doctor_data":doctor_data,
        "patient":patient
    }
    return render(request,"patientPage.html",context)
def apointDelete(request,id):
    delete_data=appointmentModel.objects.get(id=id)
    delete_data.delete()
    return redirect("apoint")
def apointEdit(request,id):
    patient_data=patientModel.objects.all()
    doctor_data=doctorModel.objects.all()
    apoint=appointmentModel.objects.get(id=id)
    if request.method=="POST":
        patient=request.POST.get("patient")
        doctor=request.POST.get("doctor")
        appointment_date=request.POST.get("appointment_date")
        status=request.POST.get("status")
        
        patient_p=patientModel.objects.get(id=patient)
        doctor_dm=doctorModel.objects.get(id=doctor)
        
        data=appointmentModel(
            id=id,
            patient=patient_p,
            doctor=doctor_dm,
            appointment_date=appointment_date,
            status=status
        )
        
        data.save()
        
        return redirect("apoint")
    context={
        "patient_data":patient_data,
        "doctor_data":doctor_data,
        "apoint":apoint
    }
    return render(request,"apointPage.html",context)
def departmentPage(request):
    department=departmentModel.objects.all()
    if request.method =="POST":
        name=request.POST.get("name")
        location=request.POST.get("location")
        
        departmentModel(
            name=name,
            location=location
        ).save()
    context={
        "department":department,
    }
    return render(request,"department.html",context)
def departEdit(request,id):
    department=departmentModel.objects.all()
    dept=departmentModel.objects.get(id=id)
    if request.method =="POST":
        name=request.POST.get("name")
        location=request.POST.get("location")
        
        departmentModel(
            id=id,
            name=name,
            location=location
        ).save()
        return redirect("department")
    context={
        "department":department,
        "dept":dept
    }
    return render(request,"departmentPage.html",context)
def departmentDelete(request,id):
    delete_data=departmentModel.objects.get(id=id)
    delete_data.delete()
    return redirect("department")