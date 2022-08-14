from django.contrib import admin

# Register your models here. daftar model yang telah kita buat
from .models import Model_pengurus, Model_santri, Model_pelanggaran1

admin.site.register(Model_pengurus)
admin.site.register(Model_santri)
admin.site.register(Model_pelanggaran1)