
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
        data = self.cleaned_data['status']
        data = AnnotationStatus.objects.get(status=data)
        return data
        

