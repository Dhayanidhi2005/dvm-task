from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from students.models import Students
from professors.models import Professors

def student_required(function):

    def wrapper(request, *args, **kwargs):
        decorated_view_func = login_required(request)
        if not decorated_view_func.user.is_authenticated:
            return decorated_view_func(request)
        try:
            Students.objects.get(user=request.user)
            return function(request, *args, **kwargs)
        except Students.DoesNotExist:
            messages.error(request,"Please log into your students account.")
            return redirect("login")
        
    return wrapper

def professor_required(function):

    def wrapper(request, *args, **kwargs):
        decorated_view_func = login_required(request)
        if not decorated_view_func.user.is_authenticated:
            return decorated_view_func(request)
        try:
            Professors.objects.get(prof=request.user)
            return function(request, *args, **kwargs)
        except Professors.DoesNotExist:
            messages.error(request,"Please log into your professors account.")
            return redirect("login")
        
    return wrapper

class StudentLoginRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        else:
            try:
                Students.objects.get(user=request.user)
                return super().dispatch(request, *args, **kwargs)
            except Students.DoesNotExist:
                messages.error(request,"Please log into your students account.")
                return redirect("login")

class ProfessorLoginRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        else:
            try:
                Professors.objects.get(prof=request.user)
                return super().dispatch(request, *args, **kwargs)
            except Professors.DoesNotExist:
                messages.error(request,"Please log into your students account.")
                return redirect("login")
            