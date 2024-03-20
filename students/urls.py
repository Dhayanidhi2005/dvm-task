from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="stu-home"),
    path("create-profile",views.ProfileCreationView.as_view(),name="create-profile"),
    path("<int:pk>",views.course_detail,name="stu-coursedetail"),
]
