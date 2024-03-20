from django import forms

class ProfileCreationForm(forms.Form):
    bitsid = forms.CharField(label="Please enter your BITS ID",max_length=13)