from django import forms
from.models import Resource, Meeting, Event

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'