from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Model_pengurus(models.Model):
	nama_pengurus	= models.CharField(max_length = 50)
	staff	=models.CharField(max_length = 10)
	no_telpon	=models.CharField(max_length = 13)
	username	=models.CharField(max_length = 20)
	password	=models.CharField(max_length = 20)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_pengurus)

class Model_santri(models.Model):
	id_santri	= models.CharField(max_length = 8)
	nama_santri	= models.CharField(max_length = 50)
	tempat_tgl_lahir	=models.CharField(max_length = 50)
	alamat	=models.CharField(max_length = 25)
	pendidikan	=models.CharField(max_length = 20)
	nama_wali	=models.CharField(max_length = 50)
	nomer_hp	=models.CharField(max_length = 13)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_santri)

class Model_pelanggaran1(models.Model):
	id_pelanggaran	= models.CharField(max_length = 10)
	nama_santri	=models.CharField(max_length = 50)
	kategori	=models.CharField(max_length = 10)
	tgl_kejadian	=models.CharField(max_length = 10)
	keterangan	=models.CharField(max_length = 60)
	hukuman	=models.CharField(max_length = 50)
	nama_pengurus	=models.CharField(max_length = 60)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.kategori)