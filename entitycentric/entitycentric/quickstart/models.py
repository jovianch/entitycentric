from django.db import models

# Create your models here.
class Barang(models.Model):
    nama = models.CharField(max_length=70)
    jenis = models.CharField(max_length=70)
    berat = models.IntegerField()

class Gudang(models.Model):
    lokasi = models.CharField(max_length=100)
    jumlah_barang = models.IntegerField()
    id_pegawai = models.CharField(max_length=50)
    id_barang = models.CharField(max_length=50)
    tanggal_masuk = models.DateField()
    tanggal_keluar = models.DateField()
