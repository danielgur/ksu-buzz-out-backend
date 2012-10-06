author__ = "danielgur2105@gmail.com (Daniel Gur)"

from tastypie import fields
from tastypie.resources import ModelResource
from listings.models import Location, Category

class LocationResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()
        resource_name = "location"

class CategoryResource(ModelResource):
    locations = fields.ToManyField(LocationResource, "location_set", null=True,
                                   full=True)

    class Meta:
        queryset = Category.objects.all()
        resource_name = "category"
        allowed_methods = [ "get" ]
