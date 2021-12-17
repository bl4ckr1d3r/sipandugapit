from django.shortcuts import render 

def index(request):
	context = {
		'title' : 'Selamat Datang di Dashboard Sistem Informasi Desa Gapit',
		'textberjalan' : 'Selamat Datang di Dashboard Sistem Informasi Desa Gapit',
		'username' : 'samsurya',
	
	}
	return render(request,'index.html', context)
	