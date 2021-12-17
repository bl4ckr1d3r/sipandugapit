from django.shortcuts import render, redirect

# Create your views here.
from .forms import DataPendudukForm
from .models import DataPenduduk

def list(request):
	if not request.user.is_authenticated:
		return redirect('login:login')
	else:
		username = request.user.username
		datapenduduk = DataPenduduk.objects.all()
		context = {
		'title' : 'Selamat Datang di Data Penduduk Sistem Informasi Desa Gapit',
		'textberjalan' : 'Selamat Datang di Data Penduduk Sistem Informasi Desa Gapit',
		'username' : username,
		'datapenduduk' : datapenduduk,
		}
		return render(request, 'datapenduduk/index.html', context)

def update(request, update_id):
	if not request.user.is_authenticated:
		return redirect('login:login')
	else:
		username = request.user.username
		updatedatapenduduk = DataPenduduk.objects.get(id=update_id)
		data = {
			'nik'			: updatedatapenduduk.nik,
	        'nama'			: updatedatapenduduk.nama,
	        'tempat'		: updatedatapenduduk.tempat,
	        'tanggal_lahir'	: updatedatapenduduk.tanggal_lahir,
	        'jenis_kelamin'	: updatedatapenduduk.jenis_kelamin,
	        'alamat'		: updatedatapenduduk.alamat,
	        'dusun'			: updatedatapenduduk.dusun,
	        'agama'			: updatedatapenduduk.agama,
	        'pekerjaan'		: updatedatapenduduk.pekerjaan,
	        'status'		: updatedatapenduduk.status,
		}
		datapendudukform = DataPendudukForm(request.POST or None, initial=data, instance=updatedatapenduduk)

		if request.method == 'POST':
			if datapendudukform.is_valid():
				datapendudukform.save()

				return redirect('datapenduduk:list')
		context = {
			'title' : 'Selamat Datang di Data Penduduk Sistem Informasi Desa Gapit',
			'textberjalan' : 'Update Data Penduduk',
			'username' : username,
			'postdatapenduduk' : datapendudukform,
		}
		return render(request, 'datapenduduk/update.html', context)
def delete(request, delete_id):
	if not request.user.is_authenticated:
		return redirect('login:login')
	else:
		DataPenduduk.objects.filter(id=delete_id).delete()
		return redirect('datapenduduk:list')

def create(request):
	if not request.user.is_authenticated:
		return redirect('login:login')
	else:
		username = request.user.username
		datapendudukform = DataPendudukForm(request.POST or None)

		if request.method == 'POST':
			if datapendudukform.is_valid():
				datapendudukform.save()

				return redirect('datapenduduk:list')
		context = {
			'title' : 'Selamat Datang di Data Penduduk Sistem Informasi Desa Gapit',
			'textberjalan' : 'Create Data Penduduk',
			'username' : username,
			'postdatapenduduk' : datapendudukform,
		}
		return render(request, 'datapenduduk/create.html', context)
