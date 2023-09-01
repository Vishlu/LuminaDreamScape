from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from . models import Company
# Register your models here.

@admin.register(Company)
class CompanyAdmin(ImportExportModelAdmin):
    list_display = ['id', 'sector']