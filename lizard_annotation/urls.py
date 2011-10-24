# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin

from lizard_ui.urls import debugmode_urlpatterns
from lizard_annotation.views import AnnotationEditView
from lizard_annotation.views import AnnotationDetailView
from lizard_annotation.views import AnnotationView

admin.autodiscover()

API_URL_NAME = 'lizard_annotation_api_root'
NAME_PREFIX = 'lizard_annotation_'

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include('lizard_annotation.api.urls')),
    url(r'^edit/',
        AnnotationEditView.as_view(),
        name='edit_view'),
    url(r'^detail/$',
        AnnotationDetailView.as_view(),
        name=NAME_PREFIX + 'detail'),
    url(r'^view/$',
        AnnotationView.as_view(),
        name=NAME_PREFIX + 'view'),
    # url(r'^something/',
    #     direct.import.views.some_method,
    #     name="name_it"),
    )
urlpatterns += debugmode_urlpatterns()
