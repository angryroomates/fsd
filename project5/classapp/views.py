from django.shortcuts import render,get_object_or_404,redirect
from classapp.models import stud,course

def courses_list(request):
    courses=course.objects.all()
    return render(request,"course_list.html",{"courses":courses})

def course_details(request,course_id):
    coursedb=get_object_or_404(course,id=course_id)
    students=coursedb.student.all()
    return render(request,"course_details.html",{"course":coursedb,"students":students})

def student_register(request,course_id):
    coursedb=get_object_or_404(course,id=course_id)
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')

        if fname and lname and email:
            student,created=stud,object.get_or_create(email=email,default={'fname':fname,'lname':lname})
            coursedb.students.add(student)
            return redirect("course_details",course_id=coursedb.id)
    return render(request,"student_register.html",{"course":coursedb})


