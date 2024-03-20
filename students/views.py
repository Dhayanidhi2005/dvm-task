from django.shortcuts import render

from professors.models import Courses
from .models import Students

# Create your views here.

def curr_student(request):
    curr_user = request.user
    return Students.objects.get(user=curr_user)

def home(request):
    curr_user = curr_student(request)
    user_courses = Courses.objects.filter(student=curr_user)
    return render(request,"students/home.html",{
        "courses":user_courses,
    })