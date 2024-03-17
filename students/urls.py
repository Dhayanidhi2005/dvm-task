from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="stu-home"),
    path("<str:course_name>",views.course_detail,name="stu-coursedetail")
]
