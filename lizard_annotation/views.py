# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

# Create your views here.

from django.views.generic import TemplateView
from django.views.generic import FormView
from lizard_annotation.forms import AnnotationForm
from lizard_annotation.models import Annotation
from lizard_annotation.models import AnnotationStatus


class AnnotationEditView(FormView):

    template_name = 'lizard_annotation/annotation_form.html'
    form_class = AnnotationForm
    # TODO Add a nice succes page
    success_url = '.'

    def form_valid(self, form):
        annotation = Annotation(**form.cleaned_data)
        annotation.save()
        return super(FormView, self).form_valid(form)

    

