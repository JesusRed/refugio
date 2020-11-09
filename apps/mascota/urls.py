from django.conf.urls import url
from apps.mascota.views import index_mascota, mascota_view, mascota_list, mascota_edit, mascota_delete, MascotaList, MascotaCreate, MascotaUpdate, MascotDelete

urlpatterns = [
    url(r'^$', index_mascota, name="mascota_form"),
    url(r'^nuevo/$', MascotaCreate.as_view(), name="mascota_crear"),
    url(r'^lista/$', MascotaList.as_view(), name="mascota_listar"),
    url(r'^editar/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name="mascota_editar"),
    url(r'^eliminar/(?P<pk>\d+)/$', MascotDelete.as_view(), name="mascota_eliminar"),
]