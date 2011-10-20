# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

from djangorestframework.resources import ModelResource
from djangorestframework.utils import as_tuple

from lizard_annotation.models import Annotation

class AnnotationResource(ModelResource):
    """
    A Communique is a GeoObject with extra metadata on that object.
    """
    model = Annotation
    fields = ()

#   # We need to override the way fields are found, since this is not a django
#   # model, but a mongoengine model.
#   @property
#   def _model_fields_set(self):
#       """
#       Return a set containing the names of validated fields on the model.
#       """

#       # model_fields = set(field.name for field in self.model._meta.fields)
#       # ^^^ Original
#       # vvv Alternative for mongoengine model instead of django model
#       model_fields = set(self.model._fields.keys())

#       if fields:
#           return model_fields & set(as_tuple(self.fields))

#       return
#       model_fields - set(as_tuple(self.exclude))
