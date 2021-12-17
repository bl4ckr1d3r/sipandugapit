from django.shortcuts import render, redirect

# Create your views here.
from .forms import DataKartuKeluargaForm
from .models import DataKartuKeluarga
from .models import AnggotaKeluarga
from .forms import AnggotaKeluargaForm

def list(request):
	if not request.user.is_authenticated:
		return redirect('login:login')
	else:
		username = request.user.username
		datakartukeluarga = DataKartuKeluarga.objects.all()
		context = {
			'title' : 'Selamat Datang di Data Kartu Keluarga Sistem Informasi Desa Gapit',
			'textberjalan' : 'Selamat Datang di Data Kartu Keluarga Sistem Informasi Desa Gapit',
			'username' : username,
			'datakartukeluarga' : datakartukeluarga,
		}
		return render(request, 'datakartukeluarga/index.html', context)

def update(request, update_id):
	if not request.user.is_authenticated:
		return redirect('login:login')
	else:
		username = request.user.username
		updatedatakartukeluarga = DataKartuKeluarga.objects.get(id=update_id)
		data = {
			'nokk'			: updatedatakartukeluarga.nokk,
	        'kepala_keluarga_id': updatedatakartukeluarga.kepala_keluarga_id,
	        'kecamatan'		: updatedatakartukeluarga.kecamatan,
	        'kabupaten'		: updatedatakartukeluarga.kabupaten,
	        'kodepos'		: updatedatakartukeluarga.kodepos,
	        'provinsi'		: updatedatakartukeluarga.provinsi,
		}
		datakartukeluargaform = DataKartuKeluargaForm(request.POST or None, initial=data, instance=updatedatakartukeluarga)

		if request.method == 'POST':
			if datakartukeluargaform.is_valid():
				datakartukeluargaform.save()

				return redirect('DataKartuKeluarga:list')
		context = {
			'title' : 'Selamat Datang di Data Kartu Keluarga Sistem Informasi Desa Gapit',
			'textberjalan' : 'Update Data Kartu Keluarga',
			'username' : username,
			'postdatapenduduk' : datakartukeluargaform,
		}
		return render(request, 'datakartukeluarga/update.html', context)
def delete(request, delete_id):
	if not request.user.is_authenticated:
		return redirect('login:login')
	else:
		DataKartuKeluarga.objects.filter(id=delete_id).delete()
		return redirect('datakartukeluarga:list')

def create(request):
	if not request.user.is_authenticated:
		return redirect('login:login')
	else:
		username = request.user.username
		datakartukeluargaform = DataKartuKeluargaForm(request.POST or None)

		if request.method == 'POST':
			if datakartukeluargaform.is_valid():
				datakartukeluargaform.save()

				return redirect('datakartukeluarga:list')
		context = {
			'title' : 'Selamat Datang di Data Kartu Keluarga Sistem Informasi Desa Gapit',
			'textberjalan' : 'Create Data Kartu Keluarga',
			'username' : username,
			'postdatapenduduk' : datakartukeluargaform,
		}
		return render(request, 'datakartukeluarga/create.html', context)

def anggotakeluargalist(request):
	if not request.user.is_authenticated:
		return redirect('login:login')
	else:
		username = request.user.username
		anggotakeluarga = AnggotaKeluarga.objects.all()
		context = {
			'title' : 'Selamat Datang di Data Kartu Keluarga Sistem Informasi Desa Gapit',
			'textberjalan' : 'Selamat Datang di Data Kartu Keluarga Sistem Informasi Desa Gapit',
			'username' : username,
			'anggotakeluarga' : anggotakeluarga,
		}
		return render(request, 'datakartukeluarga/anggota.html', context)
def anggotakeluargacreate(request):
	if not request.user.is_authenticated:
		return redirect('login:login')
	else:
		username = request.user.username
		anggotakeluargaform = AnggotaKeluargaForm(request.POST or None)

		if request.method == 'POST':
			if anggotakeluargaform.is_valid():
				anggotakeluargaform.save()

				return redirect('datakartukeluarga:anggotakeluargalist')
		context = {
			'title' : 'Selamat Datang di Data Kartu Keluarga Sistem Informasi Desa Gapit',
			'textberjalan' : 'Create Anggota keluarga Keluarga',
			'username' : username,
			'postanggotakeluarga' : anggotakeluargaform,
		}
		return render(request, 'datakartukeluarga/createanggotakeluarga.html', context)
def anggotakeluargadelete(request, delete_id):
	if not request.user.is_authenticated:
		return redirect('login:login')
	else:
		AnggotaKeluarga.objects.filter(id=delete_id).delete()
		return redirect('datakartukeluarga:anggotakeluargalist')