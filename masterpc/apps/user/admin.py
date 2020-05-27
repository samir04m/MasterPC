from django.contrib import admin
from .models import *

admin.site.register(Pc)
admin.site.register(Pc_cpu)
admin.site.register(Pc_gpu)
admin.site.register(Pc_board)
admin.site.register(Pc_ram)
admin.site.register(Pc_storage)
admin.site.register(Pc_psu)
admin.site.register(Pc_case)

