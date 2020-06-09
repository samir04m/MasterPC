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
    search_fields = ['name']
    list_display = ('name', 'id',)
    resource_class = StoreResource

class Store_cpuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['cpu__manufacturer__name', 'cpu__serie', 'cpu__model', 'store__name']
    list_display = ('cpu', 'store', 'price', 'is_available')
    resource_class = Store_cpuResource

class Store_gpuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['gpu__manufacturer__name', 'gpu__serie', 'gpu__model', 'store__name']
    list_display = ('gpu', 'store', 'price', 'is_available')
    resource_class = Store_gpuResource

class Store_boardAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['board__manufacturer__name', 'board__serie', 'board__model', 'store__name']
    list_display = ('board', 'store', 'price', 'is_available')
    resource_class = Store_boardResource

class Store_ramAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['ram__manufacturer__name', 'ram__serie', 'ram__model', 'store__name']
    list_display = ('ram', 'store', 'price', 'is_available')
    resource_class = Store_ramResource

class Store_storageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['storage__manufacturer__name', 'storage__serie', 'storage__model', 'store__name']
    list_display = ('storage', 'store', 'price', 'is_available')
    resource_class = Store_storageResource

class Store_psuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['psu__manufacturer__name', 'psu__serie', 'psu__model', 'store__name']
    list_display = ('psu', 'store', 'price', 'is_available')
    resource_class = Store_psuResource

class Store_caseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['case__manufacturer__name', 'case__serie', 'case__model', 'store__name']
    list_display = ('case', 'store', 'price', 'is_available')
    resource_class = Store_caseResource


admin.site.register(Store, StoreAdmin)
admin.site.register(Store_cpu, Store_cpuAdmin)
admin.site.register(Store_gpu, Store_gpuAdmin)
admin.site.register(Store_board, Store_boardAdmin)
admin.site.register(Store_ram, Store_ramAdmin)
admin.site.register(Store_storage, Store_storageAdmin)
admin.site.register(Store_psu, Store_psuAdmin)
admin.site.register(Store_case, Store_caseAdmin)
