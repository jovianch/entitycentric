from django.conf.urls import url, include
from rest_framework import routers
from entitycentric.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'barangs', views.BarangViewSet)
router.register(r'gudangs', views.GudangViewSet)
router.register(r'pegawais', views.PegawaiViewSet)
router.register(r'pengirimans', views.PengirimanViewSet)
router.register(r'transaksis', views.TransaksiViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]