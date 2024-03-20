from django.shortcuts import render,redirect
from django.views.generic import View

from .models import Professors,CourseList,Announcements
from .forms import AddAnnouncementForm,AddContentForm
# Create your views here.

def home(request):
    user_courses = Professors.objects.get(prof=request.user).courses.all()
    return render(request,"students/home.html",{
        "courses":user_courses,
        "prof":True,
    })

def add_announcements(request,pk):
    if request.method=="POST":
        form = AddAnnouncementForm(request.POST,request.FILES)
        if form.is_valid():
            req_course = CourseList.objects.get(pk=pk)
            req_prof = Professors.objects.get(prof=request.user)
            new_ann = Announcements(
                title = form.cleaned_data['title'],
                msg = form.cleaned_data['msg'],
                attachments = form.cleaned_data['attachments'],
                prof = req_prof,
                course = req_course,
            )
            new_ann.save()
            return redirect("prof-coursedetail",pk=req_course.pk)
    form = AddAnnouncementForm()
    return render(request,"students/create.html",{
        "form":form,
    })

class ContentCreateView(View):
    def get(self,request,*args, **kwargs):
        form = AddContentForm()
        return render(request,"students/create.html",{
            "form":form,
        })
    
    def post(self,request,*args, **kwargs):
        form = AddContentForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.course = CourseList.objects.get(pk=kwargs["pk"])
            obj.save()
            return redirect("prof-coursedetail",pk=kwargs["pk"])
        return render(request,"students/create.html",{
            "form":form,
        })
    