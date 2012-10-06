from django.conf.urls import patterns, include, url
from listings.api import CategoryResource

from django.contrib import admin
admin.autodiscover()

category_resource = CategoryResource()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(category_resource.urls)),
)
