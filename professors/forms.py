from django import forms

from professors.models import Content


class AddAnnouncementForm(forms.Form):
    title= forms.CharField(max_length=100)
    msg = forms.CharField(widget=forms.Textarea)
    attachments = forms.FileField(required=False)

class AddContentForm(forms.ModelForm):
    class Meta:
        model = Content
        exclude = ["course"]