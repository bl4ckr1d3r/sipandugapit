from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	if not request.user.is_authenticated:
		return redirect('login:login')
	else :
		username = request.user.username
		context = {
			'title' : 'Selamat Datang di Dashboard Sistem Informasi Desa Gapit',
			'textberjalan' : 'Selamat Datang di Dashboard Sistem Informasi Desa Gapit',
			'username' : username,
		}
		return render(request, 'dashboard/index.html', context)
