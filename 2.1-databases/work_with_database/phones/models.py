from django.db import models


class Phone(models.Model):

    name = models.CharField(max_length=50, null=False)
    price = models.PositiveIntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True)
