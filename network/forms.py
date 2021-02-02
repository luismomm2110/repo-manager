from django.forms import ModelForm
from network.models import Tag 
from django import forms

class RepoForm(ModelForm):
    class Meta: 
        model = Tag 
        fields = ['name']

class  DelForm(ModelForm):
    class Meta:
        fields  =   ['name']
    

class EditForm(forms.Form):
    newName = forms.CharField(label="New Name")