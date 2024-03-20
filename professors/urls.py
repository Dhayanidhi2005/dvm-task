from django.urls import path
from . import views
from students.views import course_detail

urlpatterns = [
    path("",views.home,name="prof-home"),
    path("<int:pk>",course_detail,name="prof-coursedetail"),
    path("<int:pk>/add-announcement",views.add_announcements,name="add-announce"),
    path("<int:pk>/add-content",views.ContentCreateView.as_view(),name="add-content"),

]
