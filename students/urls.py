from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="stu-home"),
    path("create-profile",views.ProfileCreationView.as_view(),name="create-profile"),
    path("courses/registration",views.course_registration,name="course-reg"),
    path("courses/registration/<int:pk>",views.add_enrolled_course,name="course-add"),
    path("courses/<int:pk>",views.course_detail,name="stu-coursedetail"),
]
