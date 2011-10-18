# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

# Create your views here.

from django.views.generic import FormView
<<<<<<< HEAD
from django.utils.translation import pgettext
from django.utils.translation import ugettext
=======
from django.views.generic import TemplateView
>>>>>>> a3c31f11a55caeda5ffe5d5c09cdfbe6520b4cfd
from lizard_annotation.forms import AnnotationForm
from lizard_annotation.models import Annotation
from lizard_annotation.models import AnnotationStatus
from lizard_map.views import AppView

from lizard_annotation.mongodb_queries import annotations_list

class AnnotationEditView(FormView):

    template_name = 'lizard_annotation/annotation_form.html'
    form_class = AnnotationForm
    # TODO Add a nice success page
    success_url = '.'

    def form_valid(self, form):
        Annotation(**form.cleaned_data).save()
        return super(FormView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        """ Add extra label context to the context data."""
        context = super(AnnotationEditView, self).get_context_data(**kwargs)
        
        kwargs.update({
            'label': {
                'save': pgettext(__name__, u'Save'),
                'load': ugettext(u'Load'),
            },       
        })

        return kwargs


class AnnotationView(AppView):

    template_name = 'lizard_annotation/annotation_view.html'

    def annotations(self):
        return annotations_list("Gebied100")

    def aanafvoergebiedden(self):
        aanafvoergebiedden = [{ "name": "Gebied", "id": 100 },
                             { "name": "Gebied", "id": 200 }]
        return aanafvoergebiedden
