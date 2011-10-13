
from django import forms
from models import Annotation
from models import AnnotationStatus

STATUS = (
    ('New', 'New'),
    ('Old', 'Old'),
)

class AnnotationForm(forms.Form):
    """Form for editing of annotations."""
    title = forms.CharField()

    status = forms.ChoiceField(
        choices=STATUS,
    )

    def clean_status(self):
        """Return the status object."""
        status = self.cleaned_data['status']
        obj = AnnotationStatus.objects.get(status=status)
        return obj
        

