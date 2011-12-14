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
    # Journaling
    created_by = forms.CharField(
        label=ugettext(u'Created by'),
    )
    date_created = forms.DateField(
        required=False,
        label=ugettext('Date created'),
        widget=forms.DateInput,
    )
    time_created = forms.TimeField(
        required=False,
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

    def clean_reference_objects(self):
        """
        Coerce eference_objects from JSON to python and vice versa.

        Vice versa, because form cleaning is invoked both for displaying
        a form in the html representation of the api, and for cleaning
        posted content by the form. In the first case it should be
        converted to JSON, in the latter case to python, including
        instantiating each reference object, verifying its existence
        and filling in its filter and unicode.
        """
        if isinstance(self.data['reference_objects'], dict):
            # This is the case when the form data comes really from
            # the client. Yes, restframework does this to prepopulate the
            # forms in html representation.
            self.data['reference_objects'] = simplejson.dumps(
                self.data['reference_objects'],
            )

        if isinstance(self.data['reference_objects'], unicode):
            # This is the case when the form
            # data comes really from the client.
            ref_dict = simplejson.loads(self.data['reference_objects'])
            ref_objs = {}
            for r_old in ref_dict.values():
                r_new = ReferenceObject()
                r_new.reference_model = r_old['reference_model']
                r_new.reference_id = r_old['reference_id']
                try:
                    model = load_object(r_new.reference_model)
                except:
                    raise forms.ValidationError('Reference model not found')
                try:
                    reference_object = model.objects.get(pk=r_new.reference_id)
                except:
                    raise forms.ValidationError('Reference object not found')
                # Use its name and reconstruct the filter
                r_new.reference_name = unicode(reference_object)
                r_new.reference_filter = (
                    r_new.reference_model.replace('.', '_') +
                    ':' + r_new.reference_id)
                ref_objs[r_new.reference_filter] = r_new
            return ref_objs

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
