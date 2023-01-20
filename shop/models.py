from django.db import models


class Tag(models.Model):
    name=models.CharField(max_length=50, unique=True)
    slug=models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/tag/{self.slug}/'

class Product(models.Model):
    product_code = models.AutoField(primary_key=True)
    product_name = models.CharField(null=False, max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField(null=False)
    filename = models.CharField(null=True, blank=True, default="", max_length=500)
    #tags = models.ManyToManyField(Tag, blank=True)

