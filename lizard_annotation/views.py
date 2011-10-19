# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

# Create your views here.

from django.views.generic import FormView
from django.utils.translation import pgettext 
from django.utils.translation import ugettext
from django.views.generic import TemplateView
from django.views.generic import DetailView

from lizard_annotation.forms import AnnotationForm
from lizard_annotation.models import Annotation
from lizard_annotation.models import AnnotationStatus
from lizard_ui.views import ViewContextMixin
from lizard_map.views import AppView

from lizard_annotation.mongodb_queries import annotations_list

class AnnotationDetailView(ViewContextMixin, DetailView):

    template_name = 'lizard_annotation/annotation_form.html'


class AnnotationEditView(ViewContextMixin, FormView):

    template_name = 'lizard_annotation/annotation_form.html'
    form_class = AnnotationForm
    # TODO Add a nice success page
    success_url = '.'

    labels = {
        'save': pgettext(u'Save the contents of a form', 'Save'),
    }

    def form_valid(self, form):
        Annotation(**form.cleaned_data).save()
        return super(FormView, self).form_valid(form)


class AnnotationView(TemplateView):

    template_name = 'lizard_annotation/annotation_view.html'

    def annotations(self, reference_filter=""):
        if reference_filter=="":
            return []
        else:
            return annotations_list(reference_filter)

    def reference_objects(self):
        """Return a list of dicts with reference_id and reference_model."""
        objs = {}
        for an in Annotation.objects.all():
            objs.update(an.reference_objects)
        return objs.values()

    def post(self, request, *args, **kwargs):
        reference_filter = request.POST.get('reference_filter')
        context = super(AnnotationView, self).get_context_data(**kwargs)
        #options = {"annotations": self.annotations(reference_filter)}
        return context

    def get_context_data(self, **kwargs):
        context = super(AnnotationView, self).get_context_data(**kwargs)
        return {'annotations': self.annotations(),
                'reference_objects': self.reference_objects()}

