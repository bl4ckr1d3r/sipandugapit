from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

def index(request) :

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)		
			return redirect('dashboard:index')
		else :
			messages.error(request, 'Wrong Username/Password')
			return redirect('login:login')
	context = {
		'judul' : 'Selamat Datang di Login Page',
		'pesan' : ('Selamat datang di Login'),
	}
	return render(request,'login/index.html', context)

def logoutview(request):
	logout(request)
	return redirect('login:login')
