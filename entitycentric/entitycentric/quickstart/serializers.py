from django.contrib.auth.models import User, Group
from .models import Barang, Gudang, Pegawai, Pengiriman, Transaksi
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class BarangSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Barang
        fields = ('nama', 'jenis', 'berat')

class GudangSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gudang
        fields = ('lokasi', 'jumlah_barang', 'id_pegawai', 'id_barang', 'tanggal_masuk', 'tanggal_keluar')

class PegawaiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pegawai
        fields = ('nama', 'alamat', 'telepon')

class PengirimanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pengiriman
        fields = ('id_pegawai', 'id_barang', 'tujuan', 'id_gudang')

class TransaksiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaksi
        fields = ('tanggal', 'biaya', 'id_pegawai', 'id_barang')