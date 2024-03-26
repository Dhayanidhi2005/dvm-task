from django.db import models
from django.contrib.auth.models import User
from students.models import Students

# Create your models here.

def custom_path_for_announcement(instance, filename): 
    return f"announcements/{ instance.course.course_name }/{filename}"

def custom_path_for_content(instance, filename): 
    return f"content/{ instance.course.course_name }/{filename}"

class Department(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self) :
        return f"{self.department} Department"
    
class Branch(models.Model):
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    branch = models.CharField(max_length=50)
    branch_code = models.CharField(max_length=2)

    def __str__(self) :
        return f"{self.branch}({self.dept.department} Department)"
    
    class Meta:
        verbose_name_plural = "Branches"
    
class CourseList(models.Model):

    cdc_choices = [
        ("FY","First Year"),
        ("SY1","Second Year Sem 1"),
        ("SY2","Second Year Sem 1"),
        ("TY1","Third Year Sem 1"),
        ("TY2","Third Year Sem 2"),
        ("4Y1","Fourth Year Sem 1"),
        ("4Y2","Fourth Year Sem 2"),
    ]

    electives_choices = [
        ("DEL","Department Elective"),
        ("OPEL","Open Elective"),
        ("HEL","Humanities Elective"),
    ]

    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    credit = models.IntegerField()
    course_id = models.CharField(max_length=10)
    course_name = models.CharField(max_length=100)
    cdcs = models.CharField(max_length=3,choices=cdc_choices,blank=True)
    #so that in case of electrical dept we know it is cdc of which branch
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)    
    electives = models.CharField(max_length=4,choices=electives_choices,blank=True)

    def __str__(self) :
        return f"{self.course_name}"
    
    class Meta:
        verbose_name_plural = "Course List"

class Courses(models.Model):
    course = models.ForeignKey(CourseList,on_delete = models.CASCADE)    
    student = models.ForeignKey(Students,on_delete=models.CASCADE)
    marks = models.IntegerField()
    grade=models.CharField(max_length=2,null=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.course_name}:{self.student.bitsid}"
    
    class Meta:
        unique_together = ("student", "course","date_added")
        verbose_name_plural = "Courses"

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
    courses = models.ManyToManyField(CourseList,related_name="prof")

    def __str__(self): 
        return f"{self.prof.first_name } {self.prof.last_name}"
    
    class Meta:
        verbose_name_plural = "Professors"

class Announcements(models.Model):
    title = models.CharField(max_length=100)
    msg = models.TextField()
    attachments = models.FileField(upload_to=custom_path_for_announcement)
    prof = models.ForeignKey(Professors,on_delete=models.SET_NULL,null=True)
    course = models.ForeignKey(CourseList,on_delete=models.CASCADE)

    def __str__(self) :
        return f"{self.title}"
    
    class Meta:
        verbose_name_plural = "Announcements"
    
class Content(models.Model):
    title = models.CharField(max_length=100)
    attachments = models.FileField(upload_to=custom_path_for_content)
    course = models.ForeignKey(CourseList,on_delete=models.CASCADE)

    def __str__(self) :
        return f"{self.title}"

class Evals(models.Model):
    title = models.CharField(max_length=100)
    total_marks = models.IntegerField()
    course = models.ForeignKey(CourseList,on_delete=models.CASCADE)
    student = models.ForeignKey(Students,on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)

    def __str__(self) :
        return f"{self.student.bitsid}'s {self.title}"