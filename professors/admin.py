from django.contrib import admin
from .models import Professors,Department,Courses,Announcements,Content

# Register your models here.

admin.site.register(Professors)
admin.site.register(Department)
admin.site.register(Courses)
admin.site.register(Announcements)
admin.site.register(Content)