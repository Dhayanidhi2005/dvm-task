from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import View
from django.views.generic.edit import CreateView

from .models import Professors,CourseList,Announcements,Courses,Evals
from .forms import AddAnnouncementForm,AddContentForm,AddEvalsForm,AddMarksForm
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
    
class EvalCreateView(CreateView):
    form_class = AddEvalsForm
    template_name = "students/create.html"

    def form_valid(self, form) :
        form.instance.course = CourseList.objects.get(pk=self.kwargs['pk'])
        req_stu_course = Courses.objects.get(course=form.instance.course,student=form.instance.student)
        req_stu_course.marks +=form.instance.marks
        req_stu_course.save()
        return super(EvalCreateView,self).form_valid(form)

    def get_success_url(self):
        return reverse("prof-coursedetail",kwargs={"pk":self.kwargs['pk']})
    
class AddMarkView(CreateView):
    form_class = AddMarksForm
    template_name = "students/create.html"

    def get_form_kwargs(self,**kwargs):
        #gets the current course id
        form_kwargs = super(AddMarkView, self).get_form_kwargs(**kwargs)
        form_kwargs["course_pk"] = self.kwargs["pk"]
        return form_kwargs

    def form_valid(self, form) :
        #for adding instance of eval before saving the object
        form.instance.course = CourseList.objects.get(pk=self.kwargs['pk'])
        req_stu_course = Courses.objects.get(course=form.instance.course,student=form.instance.student)
        req_stu_course.marks +=form.instance.marks
        req_stu_course.save()
        ex_eval = Evals.objects.get(title=self.kwargs['title'])
        form.instance.title = ex_eval.title
        form.instance.total_marks = ex_eval.total_marks
        return super(AddMarkView,self).form_valid(form)

    def get_success_url(self):
        return reverse("prof-coursedetail",kwargs={"pk":self.kwargs['pk']})