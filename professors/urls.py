from django.urls import path
from . import views

urlpatterns = [
    path("courses",views.home,name="prof-home"),
    path("courses/add-course",views.AddCourseView.as_view(),name="add-course"),
    path("courses/<int:pk>",views.prof_course_detail,name="prof-coursedetail"),
    path("courses/<int:pk>/students/add",views.add_students,name="add-students"),
    path("courses/<int:pk>/announcement/add",views.add_announcements,name="add-announce"),
    path("courses/<int:pk>/announcement/<int:announce_pk>/update",views.AnnouncementUpdateView.as_view(),name="update-announce"),
    path("courses/<int:pk>/announcement/<int:announce_pk>/delete",views.AnnouncementDeleteView.as_view(),name="delete-announce"),
    path("courses/<int:pk>/content/add",views.ContentCreateView.as_view(),name="add-content"),
    path("courses/<int:pk>/content/<int:content_pk>/update",views.ContentUpdateView.as_view(),name="update-content"),
    path("courses/<int:pk>/content/<int:content_pk>/delete",views.ContentDeleteView.as_view(),name="delete-content"),
    path("courses/<int:pk>/grades/add",views.add_final_grade,name="add-grades"),
    path("courses/<int:pk>/evals/add",views.EvalCreateView.as_view(),name="add-evals"),
    path("courses/<int:pk>/evals/<str:title>/marks/add",views.AddMarkView.as_view(),name="add-eval-mark"),
    path("courses/<int:pk>/evals/<str:title>/marks/select-student",views.eval_select_student,name="select-eval-student"),
    path("courses/<int:pk>/evals/<str:title>/marks/<int:eval_pk>",views.MarkUpdateView.as_view(),name="update-marks"),
]
