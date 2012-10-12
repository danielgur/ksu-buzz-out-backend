author__ = "danielgur2105@gmail.com (Daniel Gur)"

from django.db import models

class Category(models.Model):
    """The attributes for a category"""
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Location(models.Model):
    """The attributes for a location"""
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=20, blank=True)
    zip = models.CharField(max_length=5, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=40, blank=True)
    website = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=300, blank=True)
    latitude = models.DecimalField(max_digits=19, decimal_places=10, blank=True)
    longitude = models.DecimalField(max_digits=19, decimal_places=10, blank=True)
    image = models.ImageField("Picture", upload_to="uploaded_images/",
                              blank=True, null=True)
    active = models.BooleanField()
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name
