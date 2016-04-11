from django.conf.urls import url, include, patterns
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy


from photologue.views import PhotoListView, PhotoDetailView, GalleryListView, GalleryDetailView

urlpatterns = [ 
    url(r'^$',
	GalleryListView.as_view(),
        name='gallery-list'),

]
