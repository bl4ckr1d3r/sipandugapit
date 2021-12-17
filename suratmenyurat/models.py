from django.db import models

from datapenduduk.models import DataPenduduk
# Create your models here.

class SKU(models.Model):
	id = models.AutoField(primary_key= True)
	nomor = models.CharField(max_length=100)
	TANDATANGAN = (
		('Kepala Desa', 'AMAN'),
		('Sekertaris Desa', 'Muhammad Yakub'),
	)
	tanda_tangan = models.CharField(
		max_length=100,
		choices = TANDATANGAN,
		default = 'Kepala Desa',
		)
	penduduk = models.ForeignKey(DataPenduduk, on_delete=models.CASCADE)
	jenis = models.CharField(max_length=100)
	jumlah = models.CharField(max_length=100)
	status = models.CharField(max_length=100)
	mulai = models.CharField(max_length=100)
	JENIS_SKU = (
		('SKU PETANI', 'SKU PETANI'),
		('SKU TAMBAK', 'SKU TAMBAK'),
		('SKU PETERNAK', 'SKU PETERNAK'),
		('SKU KIOS', 'SKU KIOS'),
	)
	jenis_sku = models.CharField(
		max_length=100,
		choices=JENIS_SKU,
		default = 'SKU PETANI',
		)

	def __str__ (self):
			return "{}".format(self.nomor)