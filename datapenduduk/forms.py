from django import forms

from .models import DataPenduduk

class DataPendudukForm(forms.ModelForm):
    class Meta:
        model = DataPenduduk
        fields = [
        	'nik',
        	'nama',
        	'tempat',
        	'tanggal_lahir',
        	'jenis_kelamin',
            'alamat',
        	'dusun',
        	'agama',
        	'pekerjaan',
            'status',
            'pendidikan_terakhir',
        ]
        widgets= {
            'nik' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Masukan Nomor Induk Kependudukan',
                }
            ),
            'nama' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Masukan Nama Penduduk',
                }
            ),
            'tempat' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Tempat Lahir',
                }
            ),
            'tanggal_lahir' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'tahun-bulan-tanggal ex: 2001-04-16',
                }
            ),
            'jenis_kelamin' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                }
            ),
            'alamat' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'ex:RT 014 RW 008',
                }
            ),
            'jenis_kelamin' : forms.RadioSelect(
            ),
            'dusun' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                }
            ),
            'agama' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                }
            ),
            'pekerjaan' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                }
            ),
            'status' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                }
            ),
            'pendidikan_terakhir' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                }
            ),
        }