from django.contrib import admin

# Register your models here.
from .models import DataKartuKeluarga
from .models import AnggotaKeluarga

admin.site.register(DataKartuKeluarga)
admin.site.register(AnggotaKeluarga)