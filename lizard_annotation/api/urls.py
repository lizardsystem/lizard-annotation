# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin

from djangorestframework.views import InstanceModelView

from lizard_annotation.api.resources import AnnotationResource

from lizard_annotation.api.views import RootView
from lizard_annotation.api.views import AnnotationRootView
from lizard_annotation.api.views import AnnotationView
from lizard_annotation.api.views import AnnotationStatusView
from lizard_annotation.api.views import AnnotationCategoryView
from lizard_annotation.api.views import AnnotationTypeView

admin.autodiscover()

NAME_PREFIX = 'lizard_annotation_api_'

urlpatterns = patterns(
    '',
    url(r'^$',
        RootView.as_view(),
        name=NAME_PREFIX + 'root'),
    url(r'^annotation/$',
        AnnotationRootView.as_view(),
        name=NAME_PREFIX + 'annotation_root'),
    url(r'^annotation/(?P<pk>[0-9a-f]+)/$',
        AnnotationView.as_view(),
        name=NAME_PREFIX + 'annotation'),
    url(r'^status/(?P<pk>[0-9a-f]+)/$',
        AnnotationStatusView.as_view(),
        name=NAME_PREFIX + 'status'),
    url(r'^category/(?P<pk>[0-9a-f]+)/$',
        AnnotationCategoryView.as_view(),
        name=NAME_PREFIX + 'category'),
    url(r'^type/(?P<pk>[0-9a-f]+)/$',
        AnnotationTypeView.as_view(),
        name=NAME_PREFIX + 'type'),
    )
