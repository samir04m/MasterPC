from django.contrib import admin
from .models import *

admin.site.register(Manufacturer)
admin.site.register(Cpu)
admin.site.register(Gpu)
admin.site.register(Board)
admin.site.register(Ram)
admin.site.register(Psu)
admin.site.register(Case)
admin.site.register(Storage)
