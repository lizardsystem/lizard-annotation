from django import forms
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


def _clean_annotation_type(form_object):
    """Return the Annotationtype object."""
    annotation_type = form_object.cleaned_data['annotation_type']
    obj = AnnotationType.objects.get(annotation_type=annotation_type)
    return obj


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
    # References
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
    # TODO Something with the objects, workspaces, etc.
    # Journaling
    created_by = forms.CharField(
        label=ugettext(u'Created by'),
    )
    date_created = forms.DateField(
        label=ugettext('Date created'),
        widget=forms.DateInput,
    )
    time_created = forms.TimeField(
        label=ugettext('Time created'),
        widget=forms.TimeInput,
    )
    modified_by = forms.CharField(
        required=False,
        label=ugettext(u'Modified by'),
    )
    date_modified = forms.DateField(
        required=False,
        label=ugettext('Date modified'),
        widget=forms.DateInput,
    )
    time_modified = forms.TimeField(
        required=False,
        label=ugettext('Time modified'),
        widget=forms.TimeInput,
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

    clean_annotation_type = _clean_annotation_type

    def clean(self):
        return wrap_datetime(self.cleaned_data)


class StatusForm(forms.Form):
    """Form for editing of statuses."""
    status = forms.CharField(
        label=ugettext(u'Annotation status'),
    )
    annotation_type = forms.ChoiceField(
        label=ugettext(u'Annotation type'),
        choices=annotation_type_choices,
    )

    clean_annotation_type = _clean_annotation_type


class CategoryForm(forms.Form):
    """Form for editing of categories."""
    category = forms.CharField(
        label=ugettext(u'Annotation category'),
    )
    annotation_type = forms.ChoiceField(
        label=ugettext(u'Annotation type'),
        choices=annotation_type_choices,
    )

    clean_annotation_type = _clean_annotation_type


class TypeForm(forms.Form):
    """Form for editing of types."""
    annotation_type = forms.CharField(
        label=ugettext(u'Annotation type'),
    )
