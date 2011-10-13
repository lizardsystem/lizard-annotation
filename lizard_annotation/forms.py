
from django import forms
from models import Annotation

class AnnotationForm(forms.Form):
    title = forms.CharField()
