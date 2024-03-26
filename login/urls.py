from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("",auth_views.LoginView.as_view(template_name="login/login.html"),name="login"),
    path("logout/",views.logout_view,name="logout") #should be post 
]
