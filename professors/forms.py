from django import forms
from django.core.exceptions import ValidationError

from .models import Content,Evals,CourseList,Courses
from students.models import Students


class AddAnnouncementForm(forms.Form):
    title= forms.CharField(max_length=100)
    msg = forms.CharField(widget=forms.Textarea)
    attachments = forms.FileField(required=False)

class AddContentForm(forms.ModelForm):
    class Meta:
        model = Content
        exclude = ["course"]

class AddEvalsForm(forms.ModelForm):
    class Meta:
        model = Evals
        exclude = ["course"]
        
class AddMarksForm(forms.ModelForm):

    def __init__(self, course_pk,*args, **kwargs) :
        #to show only the students who are enrolled in the course.
        super(AddMarksForm,self).__init__(*args, **kwargs)
        self.fields["student"].queryset = Students.objects.filter(courses__course__pk=course_pk)

    def clean(self):
        # To check for the duplication of data.

        cleaned_data = self.cleaned_data
        name = cleaned_data.get('student')
        mark = cleaned_data.get('marks')

        matching_courses = Evals.objects.filter(student=name,marks=mark)
        if self.instance:
            matching_courses = matching_courses.exclude(pk=self.instance.pk)
        if matching_courses.exists():
            msg = f"{name}'s marks have already been uploaded."
            raise ValidationError(msg)
        else:
            return self.cleaned_data


    class Meta:
        model = Evals
        fields = ["student","marks"]

class AddGradesForm(forms.Form):
    a= forms.IntegerField(label="Enter no of people for whom A should be added",min_value=0)
    a_= forms.IntegerField(label="Enter no of people for whom A- should be added",min_value=0)
    b= forms.IntegerField(label="Enter no of people for whom B should be added",min_value=0)
    b_= forms.IntegerField(label="Enter no of people for whom B- should be added",min_value=0)
    c= forms.IntegerField(label="Enter no of people for whom C should be added",min_value=0)
    c_= forms.IntegerField(label="Enter no of people for whom C- should be added",min_value=0)
    d= forms.IntegerField(label="Enter no of people for whom D should be added",min_value=0)
    e= forms.IntegerField(label="Enter no of people for whom E should be added",min_value=0)
    nc = forms.IntegerField(label="Enter no of people for whom NC should be added",min_value=0)

class AddCourseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddCourseForm, self).__init__(*args, **kwargs)
        self.fields['branch'].required = False

    class Meta:
        model = CourseList
        fields = "__all__"
        labels = {
            "dept": "Department",
            "course_id": "Course ID",
            "course_name": "Course Name",
            "cdcs":"CDCs",
        }

class AddStudentsForm(forms.ModelForm):

    class Meta:
        model = Courses
        fields = ["student"]

class UpdateStudentMarks(forms.Form):

    required_student = forms.ChoiceField(label="Select Student for updating marks")

    def __init__(self, pk,*args, **kwargs) :
        #to give only the students who are enrolled in the course.
        super(UpdateStudentMarks,self).__init__(*args, **kwargs)
        self.fields["required_student"].choices = [
             (choice.pk, choice) for choice in Students.objects.filter(courses__course__pk=pk)
         ]
        
        