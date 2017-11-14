from django.contrib.auth.models import User, Group
from .models import Barang, Gudang, Pegawai, Pengiriman, Transaksi
from rest_framework import viewsets
from entitycentric.quickstart.serializers import UserSerializer, GroupSerializer, BarangSerializer, GudangSerializer, PegawaiSerializer, PengirimanSerializer, TransaksiSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BarangViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Barang.objects.all()
    serializer_class = BarangSerializer

class GudangViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Gudang.objects.all()
    serializer_class = GudangSerializer

class PegawaiViewSet(viewsets.ModelViewSet):
    queryset = Pegawai.objects.all()
    serializer_class = PegawaiSerializer

class PengirimanViewSet(viewsets.ModelViewSet):
    queryset = Pengiriman.objects.all()
    serializer_class = PengirimanSerializer

class TransaksiViewSet(viewsets.ModelViewSet):
    queryset = Transaksi.objects.all()
    serializer_class = TransaksiSerializer