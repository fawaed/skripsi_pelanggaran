from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from Aplikasi_pelanggaran2022 import settings
from django.urls import path
# from django.contrib.auth import views
from django.contrib import admin
from . import views

from .views import index, HomeView, LogoutView, Data_Santri, Tambah_Santri, Edit_Santri, Hapus_Santri, Data_Pelanggaran, Tambah_Pelanggaran, Edit_Pelanggaran, Hapus_Pelanggaran, list_santri, Data_Pengurus, Tambah_Pengurus, Edit_Pengurus, Hapus_Pengurus, Data_Pelanggaran_pengurus, Tambah_Pelanggaran_pengurus, Edit_Pelanggaran_pengurus, Hapus_Pelanggaran_pengurus, list_santri_pengurus, LP_pelanggaran, LP_Pengurus, Menu_laporan,LP_santri
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^$',index, name="index"),
    url(r'^Home/$', HomeView, name="Home"),
    url(r'^logout/$',LogoutView, name="logout"),

    # data santri
    url(r'^Santri/$',Data_Santri, name="Santri"),
    url(r'^Tambah_Santri/$',Tambah_Santri, name="Tambah_Santri"),
    url(r'^hapus_Santri/(?P<hapus_s>[0-9]+)$',Hapus_Santri, name="hapus_Santri"),
    url(r'^edit_Santri/(?P<id_s>[0-9]+)$',Edit_Santri, name="edit_Santri"),

    # pelanggaran
    url(r'^Pelanggaran/$',Data_Pelanggaran, name="Pelanggaran"),
    url(r'^list_santri/$',list_santri, name="list_santri"),
    url(r'^Tambah_Pelanggaran/(?P<id_sp>[0-9]+)$',Tambah_Pelanggaran, name="Tambah_Pelanggaran"),
    url(r'^hapus_Pelanggaran/(?P<hapus_p>[0-9]+)$',Hapus_Pelanggaran, name="hapus_Pelanggaran"),
    url(r'^edit_Pelanggaran/(?P<id_p>[0-9]+)$',Edit_Pelanggaran, name="edit_Pelanggaran"),
    # pengurus
    url(r'^Pengurus/$',Data_Pengurus, name="Pengurus"),
    url(r'^Tambah_Pengurus/$',Tambah_Pengurus, name="Tambah_Pengurus"),
    url(r'^hapus_Pengurus/(?P<hapus_pg>[0-9]+)$',Hapus_Pengurus, name="hapus_Pengurus"),
    url(r'^edit_Pengurus/(?P<id_pg>[0-9]+)$',Edit_Pengurus, name="edit_Pengurus"),

    # # pelanggaran pengurus
    url(r'^Pelanggaran_pengurus/$',Data_Pelanggaran_pengurus, name="Pelanggaran_pengurus"),
    url(r'^list_santri_pengurus/$',list_santri_pengurus, name="list_santri_pengurus"),
    url(r'^Tambah_Pelanggaran_pengurus/(?P<id_spp>[0-9]+)$',Tambah_Pelanggaran_pengurus, name="Tambah_Pelanggaran_pengurus"),
    url(r'^hapus_Pelanggaran_pengurus/(?P<hapus_sp>[0-9]+)$',Hapus_Pelanggaran_pengurus, name="hapus_Pelanggaran_pengurus"),
    url(r'^edit_Pelanggaran_pengurus/(?P<id_pp>[0-9]+)$',Edit_Pelanggaran_pengurus, name="edit_Pelanggaran_pengurus"),
    # menu laporan
    url(r'^Menu_laporan/$',Menu_laporan, name="Menu_laporan"),
    # lp pelanggaran
    url(r'^LP_Pengurus/$',LP_Pengurus, name="LP_Pengurus"),
    url(r'^LP_pelanggaran/$',LP_pelanggaran, name="LP_pelanggaran"),
    url(r'^LP_santri/$',LP_santri, name="LP_santri"),



    path('admin/', admin.site.urls),
]
