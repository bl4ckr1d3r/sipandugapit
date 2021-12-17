from django.db import models


# Create your models here.

class DataPenduduk(models.Model):
	id = models.AutoField(primary_key= True)
	nik = models.CharField(max_length=16)
	nama = models.CharField(max_length=100)
	tempat = models.CharField(max_length=100)
	tanggal_lahir = models.DateField()
	JENIS_KELAMIN = (
		('Laki-Laki' , 'Laki-Laki'),
		('Perempuan' , 'Perempuan'),
	)
	jenis_kelamin = models.CharField(
		max_length = 50,
		choices= JENIS_KELAMIN,
		default = 'Laki-Laki',
	)
	alamat = models.CharField(max_length=100)
	DUSUN = (
		('GAPIT','GAPIT'),
		('GAPIT TIMUR' , 'GAPIT TIMUR'),
		('ABADI' , 'ABADI'),
		('NYARINYING', 'NYARINYING'),
	)
	dusun = models.CharField(
		max_length=100,
		choices = DUSUN,
		default = 'GAPIT',
	)
	AGAMA = (
		('ISLAM' , 'ISLAM'),
		('KRISTEN' , 'KRISTEN'),
		('KATOLIK' , 'KATOLIK'),
		('HINDU' , 'HINDU'),
		('BUDHA' , 'BUDHA'),
		('KONGHUCU' , 'KONGHUCU'),
	)
	agama = models.CharField(
		max_length = 100,
		choices = AGAMA,
		default = 'ISLAM',
	)
	PEKERJAAN = (
		('Belum Bekerja' , 'Belum Bekerja'),
		('Pelajar/Mahasiswa' , 'Pelajar/Mahasiswa'),
		('Petani/Pekebun' , 'Petani/Pekebun'),
		('Peternak' , 'Peternak'),
		('Wiraswasta' , 'Wiraswasta'),
		('Wirausaha' , 'Wirausaha'),
		('Pegawai Swasta' , 'Pegawai Swasta'),
		('Pegawai Negeri' , 'Pegawai Negeri'),
		('URT', 'URT'),
	)
	pekerjaan = models.CharField(
		max_length = 100,
		choices = PEKERJAAN,
		default = 'Belum Bekerja',
	)
	STATUS = (
		('Belum Kawin' , 'Belum Kawin'),
		('Kawin' , 'Kawin'),
		('Janda' , 'Janda'),
		('Duda' , 'Duda'),
		('Cerai Hidup' , 'Cerai Hidup'),
		('Cerai Mati' , 'Cerai Mati'),
	)
	status = models.CharField(
		max_length = 100,
		choices = STATUS,
		default = 'Belum Kawin',
	)
	PENDIDIKAN_TERAKHIR = (
		('Tidak Tamat SD' , 'Tidak Tamat SD'),
		('Tamat SD' , 'Tamat SD'),
		('Tamat SMP' , 'Tamat SMP'),
		('Tamat SMA' , 'Tamat SMA'),
		('Diploma 1' , 'Diploma 1'),
		('Diploma 2' , 'Diploma 2'),
		('Diploma 3' , 'Diploma 3'),
		('Strata 1' , 'Strata 1'),
		('Strata 2' , 'Strata 2'),
		('Strata 3' , 'Strata 3'),
	)
	pendidikan_terakhir = models.CharField(
		max_length = 100,
		choices = PENDIDIKAN_TERAKHIR,
		default = 'Tidak Tamat SD',
	)

	
	def __str__ (self):
			return "{}".format(self.nama)