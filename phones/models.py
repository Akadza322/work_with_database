from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=250)
    price = models.IntegerField()
    release_date = models.CharField(max_length=50)
    lte_exists = models.BooleanField()
    slug = models.SlugField(null=False, unique=True)

