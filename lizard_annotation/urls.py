# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf.urls.defaults import (
    include,
    patterns,
    url,
)

from django.contrib import admin

from lizard_annotation.views import (
    AnnotationDetailView,
    AnnotationHistoryView,
    AnnotationArchiveView,
)

from lizard_ui.urls import debugmode_urlpatterns

admin.autodiscover()

API_URL_NAME = 'lizard_annotation_api_root'
NAME_PREFIX = 'lizard_annotation_'

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include('lizard_annotation.api.urls')),
    (r'^view/(?P<annotation_id>\d+)/$',
     AnnotationDetailView.as_view(),
     {},
     "lizard_annotation.annotation"),
    (r'^form/(?P<annotation_id>\d+)/$',
     AnnotationDetailView.as_view(),
     {},
     "lizard_annotation.annotation"),
    # Annotation edit screens
    (r'^annotation_detailedit_portal/$',
    'lizard_annotation.views.annotation_detailedit_portal',
     {},
     "lizard_annotation.annotation_detailedit_portal"),
    (r'^history/(?P<annotation_id>\d+)/$',
     AnnotationHistoryView.as_view(),
     {},
     "lizard_annotation.history"),
    (r'^archive/(?P<annotation_id>\d+)/(?P<log_entry_id>\d+)/$',
     AnnotationArchiveView.as_view(),
     {},
     "lizard_annotation.archive"),
)
urlpatterns += debugmode_urlpatterns()
