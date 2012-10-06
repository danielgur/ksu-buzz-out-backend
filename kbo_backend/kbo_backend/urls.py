from django.conf.urls import patterns, include, url
from listings.api import LocationResource, CategoryResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

location_resource = LocationResource()
category_resource = CategoryResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kbo_backend.views.home', name='home'),
    # url(r'^kbo_backend/', include('kbo_backend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(location_resource.urls)),
    url(r'^apic/', include(category_resource.urls)),
)
