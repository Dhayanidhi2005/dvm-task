from django import forms
from django.core.exceptions import ValidationError

from .models import Content,Evals
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