from django.shortcuts import render,redirect
from . models import CV

# Create your views here.

def CreateCV(request):
    if request.method=='POST':
        name = request.POST.get('name')
        age= request.POST.get('age')
        place = request.POST.get('place')
        mob_no = request.POST.get('mob_no')
        email = request.POST.get('email')
        skills = request.POST.get('skills')
        full_name = request.POST.get('full_name')
        date_of_birth = request.POST.get('date_of_birth')
        sex = request.POST.get('sex')
        nationality = request.POST.get('nationality')
        school_attended = request.POST.get('school_attended')
        academic_qualifications = request.POST.get('academic_qualifications')
        certifications = request.POST.get('certifications')
        work_history = request.POST.get('work_history')

        cv = CV(name=name,age=age,place=place,mob_no=mob_no,email=email,skills=skills,full_name=full_name,date_of_birth=date_of_birth,sex=sex,nationality=nationality,school_attended=school_attended,academic_qualifications=academic_qualifications,certifications=certifications,work_history=work_history)
        cv.save()
        return redirect('/')
    return render(request,'createCv.html')
def CVView(request):
    cv = CV.objects.all()
    return render(request,'cv.html',{'cv': cv})

def index(request):
    return render(request,'index.html')
