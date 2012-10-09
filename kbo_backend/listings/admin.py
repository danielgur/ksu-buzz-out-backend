author__ = "danielgur2105@gmail.com (Daniel Gur)"

from listings.models import Location, Category
from django.contrib import admin
from django.contrib.sites.models import Site

admin.site.register(Location)
admin.site.register(Category)
admin.site.unregister(Site)
