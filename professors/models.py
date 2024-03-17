from django.db import models
from django.contrib.auth.models import User
from students.models import Students

# Create your models here.

def custom_path_for_announcement(instance, filename): 
    return f"announcements/{ instance.course.course_name }/{filename}"

def custom_path_for_content(instance, filename): 
    return f"content/{ instance.course.course_name }/{filename}"

class Department(models.Model):

    dept = models.CharField(max_length=50)
    branchs = models.JSONField()
    cdcs = models.JSONField()
    dels = models.JSONField()
    opels = models.JSONField()

class Courses(models.Model):

    course_id = models.CharField(max_length=10)
    course_name = models.CharField(max_length=20)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    students = models.ManyToManyField(Students)
    marks = models.IntegerField()
    grade=models.CharField(max_length=2)

    def __str__(self):
        return self.course_name

class Professors(models.Model):

    designation_choices = [
        ("HOD","Head of Departemnt"),
        ("PRO","Professor"),
        ("AIP","Assistant Professor"),
        ("AOP","Associate Professor"),
    ]

    prof = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=3,choices=designation_choices)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Courses)

    def __str__(self): 
        return f"{self.prof.first_name } {self.prof.last_name}"
    

class Announcements(models.Model):
    title = models.CharField(max_length=100)
    msg = models.TextField()
    attachments = models.FileField(upload_to=custom_path_for_announcement)
    prof = models.ForeignKey(Professors,on_delete=models.SET_NULL,null=True)
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)

    def __str__(self) :
        return f"{self.title}"
    
class Content(models.Model):
    title = models.CharField(max_length=100)
    attachments = models.FileField(upload_to=custom_path_for_content)
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)