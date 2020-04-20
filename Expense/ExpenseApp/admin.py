from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

@admin.register(Farhan, Nadia, FarhanFamily, Ongie, Orange)
class ViewAdmin(ImportExportModelAdmin):
	pass