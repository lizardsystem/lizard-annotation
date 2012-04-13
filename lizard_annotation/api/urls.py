# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin

from lizard_annotation.api import views

admin.autodiscover()

NAME_PREFIX = 'lizard_annotation_api_'

urlpatterns = patterns(
    '',
    url(r'^$',
        views.RootView.as_view(),
        name=NAME_PREFIX + 'root'),

    url(r'^grid/$',
        views.AnnotationGridView.as_view(),
        name=NAME_PREFIX + 'annotation_grid'),
    url(r'^annotation/$',
        views.AnnotationRootView.as_view(),
        name=NAME_PREFIX + 'annotation_root'),
    url(r'^annotation/(?P<pk>[0-9a-f]+)/$',
        views.AnnotationView.as_view(),
        name=NAME_PREFIX + 'annotation'),

    url(r'^status/$',
        views.AnnotationStatusRootView.as_view(),
        name=NAME_PREFIX + 'annotation_status_root'),
    url(r'^status/(?P<pk>[0-9a-f]+)/$',
        views.AnnotationStatusView.as_view(),
        name=NAME_PREFIX + 'status'),

    url(r'^category/$',
        views.AnnotationCategoryRootView.as_view(),
        name=NAME_PREFIX + 'annotation_category_root'),
    url(r'^category/(?P<pk>[0-9a-f]+)/$',
        views.AnnotationCategoryView.as_view(),
        name=NAME_PREFIX + 'category'),

    url(r'^type/$',
        views.AnnotationTypeRootView.as_view(),
        name=NAME_PREFIX + 'annotation_type_root'),
    url(r'^type/(?P<pk>[0-9a-f]+)/$',
        views.AnnotationTypeView.as_view(),
        name=NAME_PREFIX + 'type'),

    # Annotationform view
    url(r'^annotationform/$',
        views.AnnotationFormView.as_view(),
        name=NAME_PREFIX + 'annotationform'),
    )

