from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.mascota.views import index_mascota, mascota_view, mascota_list, mascota_edit, mascota_delete, MascotaList, MascotaCreate, MascotaUpdate, MascotDelete

urlpatterns = [
    url(r'^$', index_mascota, name="mascota_form"),
    url(r'^nuevo/$', login_required(MascotaCreate.as_view()), name="mascota_crear"),
    url(r'^lista/$', login_required(MascotaList.as_view()), name="mascota_listar"),
    url(r'^editar/(?P<pk>\d+)/$', login_required(MascotaUpdate.as_view()), name="mascota_editar"),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotDelete.as_view()), name="mascota_eliminar"),
]