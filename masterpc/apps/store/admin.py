from django.contrib import admin
from .models import *

admin.site.register(Store)
admin.site.register(Store_cpu)
admin.site.register(Store_gpu)
admin.site.register(Store_board)
admin.site.register(Store_ram)
admin.site.register(Store_storage)
admin.site.register(Store_psu)
admin.site.register(Store_case)
