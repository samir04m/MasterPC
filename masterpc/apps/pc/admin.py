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
    search_fields = ['name']
    list_display = ('name', 'id')
    resource_class = ManufacturerResource

class CpuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['manufacturer__name', 'serie', 'model']
    list_display = ('manufacturer', 'serie', 'model')
    resource_class = CpuResource

class GpuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['manufacturer__name', 'serie', 'model']
    list_display = ('manufacturer', 'serie', 'model', 'vram_size')
    resource_class = GpuResource

class BoardAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['manufacturer__name', 'serie', 'model']
    list_display = ('manufacturer', 'serie', 'model')
    resource_class = BoardResource

class RamAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['manufacturer__name', 'serie', 'model']
    list_display = ('manufacturer', 'serie', 'model', 'speed', 'size', 'size_kit')
    resource_class = RamResource

class PsuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['manufacturer__name', 'serie', 'model']
    list_display = ('manufacturer', 'serie', 'model', 'certified')
    resource_class = PsuResource

class CaseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['manufacturer__name', 'serie', 'model']
    list_display = ('manufacturer', 'serie', 'model')
    resource_class = CaseResource

class StorageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['manufacturer__name', 'serie', 'capacity']
    list_display = ('manufacturer', 'serie', 'model', 'capacity', 'storage_type', 'form_factor')
    resource_class = StorageResource

admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Cpu, CpuAdmin)
admin.site.register(Gpu, GpuAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Ram, RamAdmin)
admin.site.register(Psu, PsuAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(Storage, StorageAdmin)