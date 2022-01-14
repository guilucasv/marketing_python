from django.contrib import admin
from django.urls import path, include
from marketing.views import EmpresaViewSet
from marketing.views import AnuncioViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Empresas', EmpresaViewSet)
router.register(r'Anuncios', AnuncioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(router.urls))
]
