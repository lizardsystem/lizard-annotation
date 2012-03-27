from django import forms
from django.utils.translation import ugettext
from django.utils import simplejson
from django_load.core import load_object

from lizard_annotation.models import AnnotationStatus
from lizard_annotation.models import AnnotationCategory
from lizard_annotation.models import AnnotationType
from lizard_annotation.models import ReferenceObject

from lizard_annotation.api.utils import wrap_datetime
from lizard_annotation.api.utils import unwrap_datetime

annotation_status_choices = [(ans.annotation_status, ans.annotation_status)
                             for ans in AnnotationStatus.objects.all()]

annotation_category_choices = [(anc.annotation_category, anc.annotation_category)
                               for anc in AnnotationCategory.objects.all()]

annotation_type_choices = [(ans.annotation_type, ans.annotation_type)
                           for ans in AnnotationType.objects.all()]


def _clean_annotation_type(form_object):
    """Return the Annotationtype object."""
    annotation_type = form_object.cleaned_data['annotation_type']
    obj = AnnotationType.objects.get(annotation_type=annotation_type)
    return obj


class AnnotationForm(forms.Form):
    """
    Form for editing of annotations.

    Take notion of how djangorestframework handles this form: If the
    form validates, the data (and not the cleaned_data) is displayed in
    the form on the api page. So the clean methods are called, to see
    if there are any errors, but the original data is used.
    """

    title = forms.CharField(
        label=ugettext(u'Title'),
    )
    description = forms.CharField(
        label=ugettext('Description'),
        widget=forms.Textarea,
    )
    date_period_start = forms.DateField(
        required=False,
        label=ugettext('Start date of period'),
        widget=forms.DateInput,
    )
    time_period_start = forms.TimeField(
        required=False,
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
    reference_objects = forms.CharField(
        required=False,
        label=ugettext(u'Reference objects'),
        widget=forms.Textarea,
    )
    # TODO Something with the objects, workspaces, etc.
    def clean_annotation_status(self):
        """Return the Status object."""
        status = self.cleaned_data['annotation_status']
        obj = AnnotationStatus.objects.get(
            annotation_status=annotation_status,
        )
        return obj

    def clean_annotation_category(self):
        """Return the Category object."""
        annotation_category = self.cleaned_data['annotation_category']
        obj = AnnotationCategory.objects.get(
            annotation_category=annotation_category,
        )
        return obj

    clean_annotation_type = _clean_annotation_type

    def clean(self):
        """
        Wrap or unwrap datetime objects in the data.
        """
        # Although only necessary when GETting, always unwrap because
        # detecting the method is not trivial here.
        self.data = unwrap_datetime(self.data)
        # The return value is only used when POSTing.
        return wrap_datetime(self.cleaned_data)


class StatusForm(forms.Form):
    """Form for editing of statuses."""
    annotation_status = forms.CharField(
        label=ugettext(u'Annotation status'),
    )
    annotation_type = forms.ChoiceField(
        label=ugettext(u'Annotation type'),
        choices=annotation_type_choices,
    )

    clean_annotation_type = _clean_annotation_type


class CategoryForm(forms.Form):
    """Form for editing of categories."""
    annotation_category = forms.CharField(
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
