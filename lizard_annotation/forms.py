from django import forms
from django.forms.extras import widgets
from django.utils.translation import ugettext

from models import AnnotationStatus
from models import AnnotationCategory
from models import AnnotationType

from lizard_annotation.api.utils import wrap_datetime

annotation_status_choices = [(ans.status, ans.status)
                             for ans in AnnotationStatus.objects.all()]

annotation_category_choices = [(anc.category, anc.category)
                               for anc in AnnotationCategory.objects.all()]

annotation_type_choices = [(ans.annotation_type, ans.annotation_type)
                           for ans in AnnotationType.objects.all()]


class AnnotationForm(forms.Form):
    """Form for editing of annotations."""
    title = forms.CharField(
        label=ugettext(u'Title'),
    )
    description = forms.CharField(
        label=ugettext('Description'),
        widget=forms.Textarea,
    )
    date_period_start = forms.DateField(
        label=ugettext('Start date of period'),
        widget=forms.DateInput,
    )
    time_period_start = forms.TimeField(
        label=ugettext('Start time of period'),
        widget=forms.TimeInput,
    )
    date_period_end = forms.DateField(
        required=False,
        label=ugettext('End date of period'),
        widget=forms.DateInput,
    )
    time_period_end = forms.TimeField(
        required=False,
        label=ugettext('End time of period'),
        widget=forms.TimeInput,
    )
    status = forms.ChoiceField(
        label=ugettext(u'Status'),
        choices=annotation_status_choices,
    )
    category = forms.ChoiceField(
        label=ugettext(u'Category'),
        choices=annotation_category_choices,
    )
    annotation_type = forms.ChoiceField(
        label=ugettext(u'Annotation type'),
        choices=annotation_type_choices,
    )

    #reference_objects = mongoengine.DictField()
    # Journaling
    #date_created = mongoengine.DateTimeField()
    #created_by = mongoengine.StringField()
    #date_modified = mongoengine.DateTimeField()
    #modified_by = mongoengine.StringField()

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

    def clean(self):
        return wrap_datetime(self.cleaned_data)
