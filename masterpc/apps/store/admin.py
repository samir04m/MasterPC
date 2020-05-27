from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class StoreResource(resources.ModelResource):
    class Meta:
        model = Store

class Store_cpuResource(resources.ModelResource):
    class Meta:
        model = Store_cpu

class Store_gpuResource(resources.ModelResource):
    class Meta:
        model = Store_gpu

class Store_boardResource(resources.ModelResource):
    class Meta:
        model = Store_board

class Store_ramResource(resources.ModelResource):
    class Meta:
        model = Store_ram

class Store_storageResource(resources.ModelResource):
    class Meta:
        model = Store_storage

class Store_psuResource(resources.ModelResource):
    class Meta:
        model = Store_psu

class Store_caseResource(resources.ModelResource):
    class Meta:
        model = Store_case

class StoreAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = StoreResource

class Store_cpuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        model =  Store_cpuResource
class Store_gpuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        model =  Store_gpuResource
class Store_boardAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        model =  Store_boardResource
class Store_ramAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        model =  Store_ramResource
class Store_storageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        model =  Store_storageResource
class Store_psuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        model =  Store_psuResource
class Store_caseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        model =  Store_caseResource

admin.site.register(Store, StoreAdmin)
admin.site.register(Store_cpu, Store_cpuAdmin)
admin.site.register(Store_gpu, Store_gpuAdmin)
admin.site.register(Store_board, Store_boardAdmin)
admin.site.register(Store_ram, Store_ramAdmin)
admin.site.register(Store_storage, Store_storageAdmin)
admin.site.register(Store_psu, Store_psuAdmin)
admin.site.register(Store_case, Store_caseAdmin)
