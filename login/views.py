from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# Create your views here.

def login(request):
    if request.method=="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,user=form.get_user())
    else:
        form = AuthenticationForm()
    return render(request,"login/login.html",{
        "form":form
    })