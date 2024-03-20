from django.contrib import admin
from .models import Department,Branch,CourseList,Courses,Professors

# Register your models here.

admin.site.register(Department)
admin.site.register(Branch)
admin.site.register(CourseList)
admin.site.register(Courses)
admin.site.register(Professors)