from django import forms
from django.utils.translation import ugettext as _

from models import Annotation
from models import AnnotationStatus
from models import AnnotationCategory
from models import AnnotationType


annotation_status_choices = tuple(
    (ans.status, ans.status)
    for ans in AnnotationStatus.objects.all()
)

annotation_category_choices = tuple(
    (anc.category, anc.category)
    for anc in AnnotationCategory.objects.all()
)

annotation_type_choices = tuple(
    (ans.annotation_type, ans.annotation_type)
    for ans in AnnotationType.objects.all()
)

class AnnotationForm(forms.Form):
    """Form for editing of annotations."""
    title = forms.CharField()

    status = forms.ChoiceField(
        label=_(u'Status'),
        choices=annotation_status_choices,
    )
    category = forms.ChoiceField(
        label=_(u'Category'),
        choices=annotation_category_choices,
    )
    annotation_type = forms.ChoiceField(
        label=_(u'Annotation type'),
        choices=annotation_type_choices,
    )

    def clean_status(self):
        """Return the Status object."""
        status = self.cleaned_data['status']
        obj = AnnotationStatus.objects.get(status=status)
        return obj

    def clean_category(self):
        """Return the Category object."""
        category = self.cleaned_data['category']
        obj = AnnotationCategory.objects.get(category=category)
        return obj
        
    def clean_annotation_type(self):
        """Return the Annotationtype object."""
        annotation_type = self.cleaned_data['annotation_type']
        obj = AnnotationType.objects.get(annotation_type=annotation_type)
        return obj

