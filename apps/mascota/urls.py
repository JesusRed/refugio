from django.conf.urls import url
from apps.mascota.views import index_mascota

urlpatterns = [
    url(r'^$', index_mascota),
]