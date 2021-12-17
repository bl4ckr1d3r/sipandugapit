from django import forms

from .models import DataKartuKeluarga
from .models import AnggotaKeluarga

class DataKartuKeluargaForm(forms.ModelForm):
    class Meta:
        model = DataKartuKeluarga
        fields = [
        	'nokk',
        	'kecamatan',
        	'kabupaten',
        	'kodepos',
            'provinsi',
            'kepala_keluarga_id',
        ]
        widgets= {
            'nokk' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Masukan Nomor Kartu Keluarga',
                }
            ),
            'kepala_keluarga_id' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                }
            ),
            'kecamatan' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Kecamatan',
                }
            ),
            'kabupaten' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'kabupaten',
                }
            ),
            'kodepos' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'kodepos',
                }
            ),
            'provinsi' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'provinsi',
                }
            ),
        }

class AnggotaKeluargaForm(forms.ModelForm):
    class Meta:
        model = AnggotaKeluarga
        fields = [
            'kepala_keluarga_id',
            'anggotakeluarga_id',
            'status',
        ]
        widgets = {
            'kepala_keluarga_id' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                }
            ),
            'anggotakeluarga_id' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                }
            ),
            'status' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                }
            ),
        }