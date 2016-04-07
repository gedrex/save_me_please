from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testrest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'home.views.index', name='home'),
    url(r'^jidelni_list/', include('jidelni_listek.urls', namespace='jidelni_listek')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^gallery/', include('photogallery.urls')),
    url(r'^gallery/', include('photologue.urls', namespace='photologue')),
#    url(r'^jsonphotolist/$', PhotoJSONListView.as_view()),
#    url(r'^gallerylist/$', GalleryListView.as_view()),

)
