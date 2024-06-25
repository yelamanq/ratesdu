from django.contrib import admin
from .models import Cabinet, CabinetStatus, CabinetStatusValue
# Register your models here.

admin.site.register(Cabinet)
admin.site.register(CabinetStatus)
admin.site.register(CabinetStatusValue)