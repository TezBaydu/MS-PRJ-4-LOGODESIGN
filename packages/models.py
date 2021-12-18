from django.db import models


class Company(models.Model):

    class Meta:
        verbose_name_plural = 'Companies'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    logoimage = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Project(models.Model):
    company = models.ForeignKey(
        'Company', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Package(models.Model):

    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    logo_count_request = models.IntegerField()
    quality_request = models.TextField(null=True, blank=True)
    support_request = models.TextField(null=True, blank=True)
    production_days = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
