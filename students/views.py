from django.shortcuts import render,redirect
from django.views.generic import View

from professors.models import Courses,Professors,CourseList,Announcements,Content,Evals,Branch
from .models import Students
from .forms import ProfileCreationForm

class ProfileCreationView(View):
    def get(self,request):
        form = ProfileCreationForm()
        return render(request,"students/create.html",{
            "form":form,
        })
    def post(self,request):
        form = ProfileCreationForm(request.POST,request.FILES)
        if form.is_valid():
            curr_user = request.user
            new_profile = Students(
                user =curr_user,
                bitsid = form.cleaned_data.get('bitsid'),
            )
            new_profile.save()
            return redirect("stu-home")
        return render(request,"students/create.html",{
            "form":form,
        })

def home(request):
    try:
        curr_user = Students.objects.get(user=request.user)
        user_courses = Courses.objects.filter(student=curr_user)
        return render(request,"students/home.html",{
            "courses":user_courses,
        })
    except Students.DoesNotExist:
        return redirect("create-profile")
    
def course_detail(request,pk):
    try:
        Professors.objects.get(prof=request.user)
        prof=True
    except Professors.DoesNotExist:
        prof=False
    selected_course = CourseList.objects.get(pk=pk)
    course_annoucements = Announcements.objects.filter(course=selected_course)
    course_content = Content.objects.filter(course=selected_course)
    if prof:
        evals = Evals.objects.filter(course = selected_course).distinct()
        stu_grade = None
    else:
        curr_student = Students.objects.get(user=request.user)
        stu_grade = Courses.objects.get(course=selected_course,student=curr_student).grade
        evals = Evals.objects.filter(student=curr_student,course=selected_course)
        
    return render(request,"students/course-detail.html",{
        "course":selected_course,
        "annoucements":course_annoucements,
        "contents":course_content,
        "prof":prof,
        "evals":evals,
        "grade":stu_grade,
    })