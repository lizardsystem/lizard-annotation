# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin

from lizard_annotation.api.views import RootView

from lizard_annotation.api.views import AnnotationGridView
from lizard_annotation.api.views import AnnotationRootView
from lizard_annotation.api.views import AnnotationCreateView
from lizard_annotation.api.views import AnnotationView

from lizard_annotation.api.views import AnnotationStatusRootView
from lizard_annotation.api.views import AnnotationStatusCreateView
from lizard_annotation.api.views import AnnotationStatusView

from lizard_annotation.api.views import AnnotationCategoryRootView
from lizard_annotation.api.views import AnnotationCategoryCreateView
from lizard_annotation.api.views import AnnotationCategoryView

from lizard_annotation.api.views import AnnotationTypeRootView
from lizard_annotation.api.views import AnnotationTypeCreateView
from lizard_annotation.api.views import AnnotationTypeView

admin.autodiscover()

NAME_PREFIX = 'lizard_annotation_api_'

urlpatterns = patterns(
    '',
    url(r'^$',
        RootView.as_view(),
        name=NAME_PREFIX + 'root'),

    url(r'^grid/$',
        AnnotationGridView.as_view(),
        name=NAME_PREFIX + 'annotation_grid'),
    url(r'^annotation/$',
        AnnotationRootView.as_view(),
        name=NAME_PREFIX + 'annotation_root'),
    url(r'^annotation/create/$',
        AnnotationCreateView.as_view(),
        name=NAME_PREFIX + 'annotation_create'),
    url(r'^annotation/(?P<pk>[0-9a-f]+)/$',
        AnnotationView.as_view(),
        name=NAME_PREFIX + 'annotation'),

    url(r'^status/$',
        AnnotationStatusRootView.as_view(),
        name=NAME_PREFIX + 'annotation_status_root'),
    url(r'^status/create/$',
        AnnotationStatusCreateView.as_view(),
        name=NAME_PREFIX + 'annotation_status_create'),
    url(r'^status/(?P<pk>[0-9a-f]+)/$',
        AnnotationStatusView.as_view(),
        name=NAME_PREFIX + 'status'),

    url(r'^category/$',
        AnnotationCategoryRootView.as_view(),
        name=NAME_PREFIX + 'annotation_category_root'),
    url(r'^category/create/$',
        AnnotationCategoryCreateView.as_view(),
        name=NAME_PREFIX + 'annotation_category_create'),
    url(r'^category/(?P<pk>[0-9a-f]+)/$',
        AnnotationCategoryView.as_view(),
        name=NAME_PREFIX + 'category'),

    url(r'^type/$',
        AnnotationTypeRootView.as_view(),
        name=NAME_PREFIX + 'annotation_type_root'),
    url(r'^type/create/$',
        AnnotationTypeCreateView.as_view(),
        name=NAME_PREFIX + 'annotation_type_create'),
    url(r'^type/(?P<pk>[0-9a-f]+)/$',
        AnnotationTypeView.as_view(),
        name=NAME_PREFIX + 'type'),
    )
