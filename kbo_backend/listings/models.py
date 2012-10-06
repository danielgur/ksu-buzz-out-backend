from django.db import models

class Category(models.Model):
    """The attributes for a category"""
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Location(models.Model):
    """The attributes for a location"""
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    website = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    latitude = models.DecimalField(max_digits=19, decimal_places=10)
    longitude = models.DecimalField(max_digits=19, decimal_places=10)
    image = models.ImageField("Picture", upload_to="uploaded_images/",
                              blank=True, null=True)
    active = models.BooleanField()
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name
