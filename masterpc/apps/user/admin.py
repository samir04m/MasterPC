from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class PcResource(resources.ModelResource):
    class Meta:
        model = Pc

class Pc_cpuResource(resources.ModelResource):
    class Meta:
        model = Pc_cpu

class Pc_gpuResource(resources.ModelResource):
    class Meta:
        model = Pc_gpu

class Pc_boardResource(resources.ModelResource):
    class Meta:
        model = Pc_board

class Pc_ramResource(resources.ModelResource):
    class Meta:
        model = Pc_ram

class Pc_storageResource(resources.ModelResource):
    class Meta:
        model = Pc_storage

class Pc_psuResource(resources.ModelResource):
    class Meta:
        model = Pc_psu

class Pc_caseResource(resources.ModelResource):
    class Meta:
        model = Pc_case


class PcAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PcResource

class Pc_cpuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Pc_cpuResource

class Pc_gpuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Pc_gpuResource

class Pc_boardAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Pc_boardResource

class Pc_ramAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Pc_ramResource

class Pc_storageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Pc_storageResource

class Pc_psuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Pc_psuResource

class Pc_caseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Pc_caseResource
        
admin.site.register(Pc)
admin.site.register(Pc_cpu)
admin.site.register(Pc_gpu)
admin.site.register(Pc_board)
admin.site.register(Pc_ram)
admin.site.register(Pc_storage)
admin.site.register(Pc_psu)
admin.site.register(Pc_case)

