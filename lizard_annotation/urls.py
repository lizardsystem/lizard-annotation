# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin

from lizard_ui.urls import debugmode_urlpatterns
from lizard_annotation.views import AnnotationEditView
from lizard_annotation.views import AnnotationView
from django.views.generic import ListView

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    url(r'^edit/',
        AnnotationEditView.as_view(),
        name='edit_view'),
    url(r'^view/$',
        AnnotationView.as_view(),
        name='a_view'),
    # url(r'^something/',
    #     direct.import.views.some_method,
    #     name="name_it"),
    )
urlpatterns += debugmode_urlpatterns()
