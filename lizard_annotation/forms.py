from django_mongokit.forms import DocumentForm
from models import Annotation

class AnnotationForm(DocumentForm):

    class Meta:
            document = Annotation
