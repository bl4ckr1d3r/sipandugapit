from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
	'title' : 'Selamat Datang di Data Penduduk Sistem Informasi Desa Gapit',
	'textberjalan' : 'Selamat Datang di Data Penduduk Sistem Informasi Desa Gapit',
	'username' : 'samsurya',
	}
	return render(request, 'databpjs/index.html', context)