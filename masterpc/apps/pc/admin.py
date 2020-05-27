from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ManufacturerResource(resources.ModelResource):
    class Meta:
        model = Manufacturer

class CpuResource(resources.ModelResource):
    class Meta:
        model = Cpu

class GpuResource(resources.ModelResource):
    class Meta:
        model = Gpu

class BoardResource(resources.ModelResource):
    class Meta:
        model = Board

class RamResource(resources.ModelResource):
    class Meta:
        model = Ram

class PsuResource(resources.ModelResource):
    class Meta:
        model = Psu

class CaseResource(resources.ModelResource):
    class Meta:
        model = Case

class StorageResource(resources.ModelResource):
    class Meta:
        model = Storage

class ManufacturerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ManufacturerResource

class CpuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CpuResource

class CpuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CpuResource

class GpuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Gpu

class BoardAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Board

class RamAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Ram

class PsuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Psu

class CaseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Case

class StorageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Storage


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Cpu, CpuAdmin)
admin.site.register(Gpu, GpuAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Ram, RamAdmin)
admin.site.register(Psu, PsuAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(Storage, StorageAdmin)