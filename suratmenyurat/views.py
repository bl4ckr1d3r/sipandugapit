from django.shortcuts import render, redirect

# Create your views here.
from .forms import SKUForm
from .models import SKU

def list(request):
	if not request.user.is_authenticated:
		return redirect('login:login')
	else:
		username = request.user.username
		sku = SKU.objects.all()
		context = {
		'title' : 'Selamat Datang di Kelola Surat Sistem Informasi Desa Gapit',
		'textberjalan' : 'Selamat Datang di Kelola Surat Sistem Informasi Desa Gapit',
		'sku' : sku,
		}
		return render(request, 'suratmenyurat/index.html', context)


def create(request):
	if not request.user.is_authenticated:
		return redirect('login:login')
	else:
		username = request.user.username
		skuform = SKUForm(request.POST or None)

		if request.method == 'POST':
			if skuform.is_valid():
				skuform.save()

				return redirect('suratmenyurat:list')
		context = {
			'title' : 'Selamat Datang di Kelola Surat Sistem Informasi Desa Gapit',
			'textberjalan' : 'Create Surat ',
			'username' : username,
			'postdatasurat' : skuform,
		}
		return render(request, 'suratmenyurat/create.html', context)
def delete(request, delete_id):
	if not request.user.is_authenticated:
		return redirect('login:login')
	else:
		SKU.objects.filter(id=delete_id).delete()
		return redirect('suratmenyurat:list')

def print(request, sku_id):
	if not request.user.is_authenticated:
		return redirect('login:login')
	else:
		username = request.user.username
		cetaksku = SKU.objects.get(id=sku_id)
		data = {
			'nomor'			: cetaksku.nomor,
	        'tanda_tangan'	: cetaksku.tanda_tangan,
	        'penduduk'		: cetaksku.penduduk,
	        'jenis'			: cetaksku.jenis,
	        'jumlah'		: cetaksku.jumlah,
	        'status'		: cetaksku.status,
	        'mulai'			: cetaksku.mulai,
	        'jenis_sku'		: cetaksku.jenis_sku,
		}
		if cetaksku.jenis_sku == 'SKU PETERNAK':
			if cetaksku.tanda_tangan == 'Kepala Desa':
				context = {
					'title' : 'Cetak SKU PETANI Sistem Informasi Desa Gapit',
					'data' : data,
					'nip' : 'Nip Pak Kades',

				}
				return render(request, 'suratmenyurat/skupetani.html', context)
		sku = SKU.objects.all()
		context = {
		'title' : 'Selamat Datang di Kelola Surat Sistem Informasi Desa Gapit',
		'textberjalan' : 'Selamat Datang di Kelola Surat Sistem Informasi Desa Gapit',
		'sku' : sku,
		}
		return render(request, 'suratmenyurat/index.html', context)
