from django.conf.urls import url
from apps.mascota.views import index_mascota, mascota_view, mascota_list

urlpatterns = [
    url(r'^$', index_mascota, name="mascota_form"),
    url(r'^nuevo/$', mascota_view, name="mascota_crear"),
    url(r'^lsita/$', mascota_list, name="mascota_listar"),
]