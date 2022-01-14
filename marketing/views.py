from django.db.models import query
from rest_framework import serializers, viewsets
from marketing.models import Empresa
from marketing.models import Anuncio
from marketing.serializer import EmpresaSerializer
from marketing.serializer import AnuncioSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer
