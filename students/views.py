from django.shortcuts import render
from professors.models import Courses,Announcements,Content
from .models import Students

# Create your views here.

def curr_student(request):
    curr_user = request.user
    return Students.objects.get(user=curr_user)

def home(request):
    curr_user = curr_student(request)
    user_courses = Courses.objects.filter(students=curr_user)
    return render(request,"students/home.html",{
        "courses":user_courses,
    })

def course_detail(request,course_name):
    selected_course = Courses.objects.get(course_name=course_name)
    course_annoucements = Announcements.objects.filter(course=selected_course)
    course_content = Content.objects.filter(course=selected_course)
    return render(request,"students/course-detail.html",{
        "course":selected_course,
        "annoucements":course_annoucements,
        "contents":course_content,
    })
    