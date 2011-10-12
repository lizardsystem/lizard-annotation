# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

# Create your views here.

from django.views.generic import TemplateView
from django.views.generic import FormView
from lizard_annotation.forms import AnnotationDetailForm


class DetailView(FormView):

    template_name = 'lizard_annotation/annotation_detail.html'
    form_class = AnnotationDetailForm

