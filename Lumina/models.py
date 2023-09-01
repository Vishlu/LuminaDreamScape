from import_export.admin import ImportExportModelAdmin
from django.db import models

# Create your models here.
class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    end_year = models.CharField( max_length=200, null=True, blank=True)
    intensity = models.IntegerField(null=True, blank=True)
    sector = models.CharField( max_length=200)
    topic = models.CharField( max_length=200)
    insight = models.CharField( max_length=200)
    url = models.CharField( max_length=200)
    region = models.CharField( max_length=200, null=True, blank=True)
    start_year = models.CharField( max_length=200, null=True, blank=True)
    impact = models.CharField( max_length=200, null=True, blank=True)
    added = models.CharField( max_length=200)
    published = models.CharField( max_length=200)
    country = models.CharField( max_length=200, null=True, blank=True)
    relevance = models.IntegerField(null=True, blank=True)
    pestle = models.CharField( max_length=100)
    source = models.CharField( max_length=200)
    title = models.CharField( max_length=200)
    likelihood = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.sector