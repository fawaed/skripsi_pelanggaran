
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from .models import Model_pengurus, Model_santri, Model_pelanggaran1
import hashlib


def index(request):
	context = {
	'page_title':'Login',
	}
	#print(request.user)
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('Home')
		else:
			return redirect('index')

	return render(request, 'index.html',  context)

def HomeView(request):	
	jumlah = Model_pelanggaran1.objects.count()
	context = {
	'page_title':'Home',
	'jumlah':jumlah
	}
	test_group = Group.objects.get(name="pengurus")
	admin_group = request.user.groups.all()

	template_name = None
	if test_group in admin_group:
		template_name = 'halaman_pengurus.html'
	else:
		template_name = 'home.html'

	return render(request, template_name,  context)

def LogoutView(request):
	context = {
	'page_title':'logout',
	}
	if request.method == "POST":
		if request.POST["logout"] == "Submit":	
			logout(request)

		return redirect('index')

	return render(request, 'logout.html',  context)	

def Data_Santri(request):
	tampil_santri = Model_santri.objects.all()
	context = {	
	'tampil_santri': tampil_santri,
	}
	return render(request, 'Master_data/data_santri/tabel.html',  context)	

def Tambah_Santri(request):
	if request.method == 'POST':
		Model_santri.objects.create(
			id_santri = request.POST['id_santri'],
			nama_santri = request.POST['nama_santri'],
			tempat_tgl_lahir = request.POST['tempat_tgl_lahir'],			
			alamat = request.POST['alamat'],			
			pendidikan = request.POST['pendidikan'],			
			nama_wali = request.POST['nama_wali'],			
			nomer_hp = request.POST['nomer_hp'],			
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Santri/")	
	context = {	
	'Tambah': 'Tambah'
	}
	return render(request, 'Master_data/data_santri/tambah.html', context)

def Hapus_Santri(request, hapus_s):
	Model_santri.objects.filter(id=hapus_s).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Santri')			

def Edit_Santri(request, id_s):		
	edit_santri = Model_santri.objects.get(id=id_s)
	if request.method == 'POST':		
			edit_santri.id_santri = request.POST.get('id_santri')
			edit_santri.nama_santri = request.POST.get('nama_santri')			
			edit_santri.tempat_tgl_lahir = request.POST.get('tempat_tgl_lahir')						
			edit_santri.alamat = request.POST.get('alamat')						
			edit_santri.pendidikan = request.POST.get('pendidikan')						
			edit_santri.nama_wali = request.POST.get('nama_wali')						
			edit_santri.nomer_hp = request.POST.get('nomer_hp')						
			edit_santri.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Santri')

	context = {'edit_santri': edit_santri}
	return render(request, 'Master_data/data_santri/edit.html',  context)


# pelanggaran
def Data_Pelanggaran(request):
	data_pelanggaran = Model_pelanggaran1.objects.all()
	context = {	
	'data_pelanggaran': data_pelanggaran,
	}
	return render(request, 'Master_data/data_pelanggaran/tabel.html',  context)	

# proses pelanggaran santri
def list_santri(request):
	tampil_santri = Model_santri.objects.all()
	context = {	
	'tampil_santri': tampil_santri,
	}
	return render(request, 'Master_data/data_pelanggaran/proses_pelanggaran.html',  context)	

def Tambah_Pelanggaran(request, id_sp):
	kode = Model_santri.objects.count()
	kode_otomatis = kode + 1

	proses_santri = Model_santri.objects.get(id=id_sp)
	if request.method == 'POST':
		Model_pelanggaran1.objects.create(
			id_pelanggaran = request.POST['id_pelanggaran'],
			nama_santri = request.POST['nama_santri'],
			kategori = request.POST['kategori'],			
			tgl_kejadian = request.POST['tgl_kejadian'],			
			keterangan = request.POST['keterangan'],			
			hukuman = request.POST['hukuman'],			
			nama_pengurus = request.POST['nama_pengurus'],			
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Pelanggaran/")	
	context = {	
	'Tambah': 'Tambah',
	'proses_santri': proses_santri,
	'kode_otomatis': kode_otomatis
	}
	return render(request, 'Master_data/data_pelanggaran/tambah.html', context)

def Hapus_Pelanggaran(request, hapus_p):
	Model_pelanggaran1.objects.filter(id=hapus_p).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Pelanggaran')			

def Edit_Pelanggaran(request, id_p):		
	edit_pelanggaran = Model_pelanggaran1.objects.get(id=id_p)
	if request.method == 'POST':		
			edit_pelanggaran.id_pelanggaran = request.POST.get('id_pelanggaran')
			edit_pelanggaran.nama_santri = request.POST.get('nama_santri')			
			edit_pelanggaran.kategori = request.POST.get('kategori')						
			edit_pelanggaran.tgl_kejadian = request.POST.get('tgl_kejadian')						
			edit_pelanggaran.keterangan = request.POST.get('keterangan')						
			edit_pelanggaran.hukuman = request.POST.get('hukuman')						
			edit_pelanggaran.nama_pengurus = request.POST.get('nama_pengurus')						
			edit_pelanggaran.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Pelanggaran')

	context = {'edit_pelanggaran': edit_pelanggaran}
	return render(request, 'Master_data/data_pelanggaran/edit.html',  context)

#pengurus

def Data_Pengurus(request):
	tampil_pengurus = Model_pengurus.objects.all()
	context = {	
	'tampil_pengurus': tampil_pengurus,
	}
	return render(request, 'Master_data/data_pengurus/tabel.html',  context)	

def Tambah_Pengurus(request):
	if request.method == 'POST':
		Model_pengurus.objects.create(
			nama_pengurus = request.POST['nama_pengurus'],
			staff = request.POST['staff'],
			no_telpon = request.POST['no_telepon'],			
			username = request.POST['username'],			
			password = request.POST['password'],			
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Pengurus/")	
	context = {	
	'Tambah siswa': 'Tambah siswa'
	}
	return render(request, 'Master_data/data_pengurus/tambah.html', context)

def Hapus_Pengurus(request, hapus_pg):
	Model_pengurus.objects.filter(id=hapus_pg).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Pengurus')			

def Edit_Pengurus(request, id_pg):		
	edit_pengurus = Model_pengurus.objects.get(id=id_pg)
	if request.method == 'POST':		
			edit_pengurus.nama_pengurus = request.POST.get('nama_pengurus')
			edit_pengurus.staff = request.POST.get('staff')			
			edit_pengurus.no_telpon = request.POST.get('no_telepon')						
			edit_pengurus.username = request.POST.get('username')						
			edit_pengurus.password = request.POST.get('password')						
			edit_pengurus.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Pengurus')

	context = {'edit_pengurus': edit_pengurus}
	return render(request, 'Master_data/data_pengurus/edit.html',  context)


# pelanggaran pengurus
# pelanggaran
def Data_Pelanggaran_pengurus(request):
	data_pelanggaran = Model_pelanggaran1.objects.all()
	context = {	
	'data_pelanggaran': data_pelanggaran,
	}
	return render(request, 'Master_pengurus/data_pelanggaran/tabel.html',  context)	

# proses pelanggaran santri
def list_santri_pengurus(request):
	tampil_santri = Model_santri.objects.all()
	context = {	
	'tampil_santri': tampil_santri,
	}
	return render(request, 'Master_pengurus/data_pelanggaran/proses_pelanggaran.html',  context)	

def Tambah_Pelanggaran_pengurus(request, id_spp):
	proses_santri = Model_santri.objects.get(id=id_spp)
	if request.method == 'POST':
		Model_pelanggaran1.objects.create(
			id_pelanggaran = request.POST['id_pelanggaran'],
			nama_santri = request.POST['nama_santri'],
			kategori = request.POST['kategori'],			
			tgl_kejadian = request.POST['tgl_kejadian'],			
			keterangan = request.POST['keterangan'],			
			hukuman = request.POST['hukuman'],			
			nama_pengurus = request.POST['nama_pengurus'],	
		    )
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Pelanggaran_pengurus/")	
	context = {	
	'Tambah': 'Tambah',
	'proses_santri': proses_santri
	}
	return render(request, 'Master_pengurus/data_pelanggaran/tambah.html', context)

def Hapus_Pelanggaran_pengurus(request, hapus_sp):
	Model_pelanggaran1.objects.filter(id=hapus_sp).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Pelanggaran_pengurus')			

def Edit_Pelanggaran_pengurus(request, id_pp):		
	edit_pelanggaran = Model_pelanggaran1.objects.get(id=id_pp)
	if request.method == 'POST':		
			edit_pelanggaran.id_santri = request.POST.get('id_santri')
			edit_pelanggaran.nama_santri = request.POST.get('nama_santri')			
			edit_pelanggaran.kategori = request.POST.get('kategori')						
			edit_pelanggaran.kejadian = request.POST.get('kejadian')						
			edit_pelanggaran.keterangan = request.POST.get('keterangan')						
			edit_pelanggaran.nama_pelanggaran = request.POST.get('nama_pelanggaran')						
			edit_pelanggaran.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Pelanggaran_pengurus')

	context = {'edit_pelanggaran': edit_pelanggaran}
	return render(request, 'Master_pengurus/data_pelanggaran/edit.html',  context)

# laporan menu
def Menu_laporan(request):
	context = {	
	'menu':'menu'
	}
	return render(request, 'Master_data/laporan/menu_lp.html',  context)	

def LP_Pengurus(request):
	LP_Pengurus = Model_pengurus.objects.all()
	context = {	
	'LP_Pengurus': LP_Pengurus,
	}
	return render(request, 'Master_data/laporan/lp_pengurus.html',  context)	

def LP_pelanggaran(request):
	LP_pelanggaran = Model_pelanggaran1.objects.all()
	context = {	
	'LP_pelanggaran': LP_pelanggaran,
	}
	return render(request, 'Master_data/laporan/lp_pelanggaran.html',  context)	

def LP_santri(request):
	LP_santri = Model_santri.objects.all()
	context = {	
	'LP_santri': LP_santri,
	}
	return render(request, 'Master_data/laporan/LP_santri.html',  context)	