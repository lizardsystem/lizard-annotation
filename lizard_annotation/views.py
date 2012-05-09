# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

# Create your views here.

from lizard_map.views import AppView
from lizard_ui.views import ViewContextMixin
from lizard_area.models import Area

from django.utils.translation import pgettext
import django

from django.views.generic import (
    FormView,
    TemplateView,
    DetailView,
)

from lizard_history.utils import get_history

from lizard_annotation.forms import AnnotationForm
from lizard_annotation.models import (
    Annotation,
    AnnotationType,
    AnnotationStatus,
    AnnotationCategory,
)


class AnnotationDetailView(AppView):
    """
    Show annotation details
    """
    template_name='lizard_annotation/annotation_view.html'

    def annotation(self):
        """Return an annotation"""
        if not hasattr(self, '_annotation'):
            self._annotation = Annotation.objects.get(
                pk=self.annotation_id)
        return self._annotation

    def get(self, request, *args, **kwargs):
        self.annotation_id = kwargs['annotation_id']
        return super(AnnotationDetailView, self).get(
            request, *args, **kwargs)


def annotation_detailedit_portal(request):
    """
    Return JSON for request.
    """
    c = django.template.RequestContext(request)

    annotation_id = request.GET.get('annotation_id', None)

    init_parent = request.GET.get('parent_id', None)
    area_id = request.GET.get('area_id', None)

    if init_parent:
        init_parent = annotation.objects.get(pk=init_parent)

    init_area = None
    init_waterbody = None

    if area_id:
        area =  Area.objects.get(ident=area_id)

        if area.area_class == Area.AREA_CLASS_AAN_AFVOERGEBIED:
            init_area = area
        else:
            init_waterbody = area

    try:
        annotation = Annotation.objects.get(pk=annotation_id)
    except Annotation.DoesNotExist:
        annotation = None

    if request.user.is_authenticated():

        template = django.template.loader.get_template(
            'lizard_annotation/annotation_form.js',
        )
        context = django.template.RequestContext(request, {
            'annotation': annotation,
            'annotation_types': django.utils.simplejson.dumps(
                [{'id': t.id, 'name': str(t)}
                 for t in AnnotationType.objects.all()]
            ),
            'annotation_categories': django.utils.simplejson.dumps(
                [{'id': c.id, 'name': str(c)}
                 for c in AnnotationCategory.objects.all()]
            ),
            'annotation_statuses': django.utils.simplejson.dumps(
                [{'id': s.id, 'name': str(s)}
                 for s in AnnotationStatus.objects.all()]
            ),
            'init_parent': init_parent,
            'init_area': init_area,
            'init_waterbody': init_waterbody,
        })

    else:
        template = django.template.loader.get_template(
            'portals/geen_toegang.js',
        )
        context = None

    return django.http.HttpResponse(
        template.render(context),
        mimetype="text/plain",
    )


class AnnotationHistoryView(AppView):
    """
    Show annotation history
    """
    template_name='lizard_annotation/annotation_history.html'

    def annotation(self):
        """Return an annotation"""
        if not hasattr(self, '_annotation'):
            self._annotation = Annotation.objects.get(
                pk=self.annotation_id)
        return self._annotation

    def history(self):
        """
        Return full history, if possible cached
        """
        if not hasattr(self, '_log_entry'):
            self._history = get_history(
                obj=self.annotation(),
            )

        return self._history
    
    def get(self, request, *args, **kwargs):
        self.annotation_id = kwargs['annotation_id']
        print self.history()
        return super(AnnotationHistoryView, self).get(
            request, *args, **kwargs)


class AnnotationArchiveView(AppView):
    """
    Readonly annotation form.
    """

    def get(self, request, *args, **kwargs):
        """
        Return read only form for annotation corresponding to specific log_entry.
        """
        if request.user.is_authenticated():
            self.template_name = 'lizard_annotation/annotation_form_read_only.js'
            self.annotation_id = kwargs.get('annotation_id')
            self.log_entry_id = kwargs.get('log_entry_id')
        else:
            self.template_name = 'portals/geen_toegang.js'
        return super(AnnotationArchiveView, self).get(request, *args, **kwargs)


class AnnotationView(ViewContextMixin, TemplateView):

    template_name = 'lizard_annotation/annotation_view.html'

    def annotations(self, reference_filter=""):
        if reference_filter == "":
            return []
        else:
            return annotations_list(reference_filter)

    def reference_objects(self):
        """Return a list of dicts with reference_id and reference_model."""
        objs = {}
        for an in Annotation.objects.all():
            objs.update(an.reference_objects)
        return objs.values()
