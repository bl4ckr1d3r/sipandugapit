from django import forms

from .models import SKU

class SKUForm(forms.ModelForm):
    class Meta:
        model = SKU
        fields = [
        	'nomor',
        	'tanda_tangan',
        	'penduduk',
        	'jenis',
        	'jumlah',
            'status',
        	'mulai',
        	'jenis_sku',
        ]
        widgets= {
            'nomor' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Masukan Nomor Surat',
                }
            ),
            'tanda_tangan' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                }
            ),
            'penduduk' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                }
            ),
            'jenis' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Masukan Jenis Usaha',
                }
            ),
            'jumlah' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Masukan jumlah ternak/luas lahan/luas usaha',
                }
            ),
            'status' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Masukan Status Kepemilikan',
                }
            ),
            
            'mulai' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Masukan Waktu Pertama Memulai Usaha',
                }
            ),
            'jenis_sku' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                }
            ),
        }