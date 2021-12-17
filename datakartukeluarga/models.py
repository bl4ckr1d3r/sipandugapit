from django.db import models

from datapenduduk.models import DataPenduduk
# Create your models here.

class DataKartuKeluarga(models.Model):
	id = models.AutoField(primary_key= True)
	nokk = models.CharField(max_length=16)
	kecamatan = models.CharField(max_length=100)
	kabupaten = models.CharField(max_length=100)
	kodepos = models.CharField(max_length=100)
	provinsi = models.CharField(max_length=100)
	kepala_keluarga_id = models.ForeignKey(DataPenduduk, on_delete=models.CASCADE)
	def __str__ (self):
		return "{}".format(self.kepala_keluarga_id)

class AnggotaKeluarga(models.Model):
	id = models.AutoField(primary_key= True)
	kepala_keluarga_id = models.ForeignKey(DataKartuKeluarga, on_delete=models.CASCADE)
	anggotakeluarga_id = models.ForeignKey(DataPenduduk, on_delete=models.CASCADE)	
	STATUS = (
		('Istri', 'Istri'),
		('Anak Kandung', 'Anak Kandung'),
		('Anak Tiri', 'Anak Tiri'),
	)
	status = models.CharField(
		max_length=100,
		choices = STATUS,
		default = 'Istri',
		)
	def __str__ (self):
		return "{}".format(self.id)