from rest_framework import serializers
from marketing.admin import Anuncios
from marketing.models import Empresa
from marketing.models import Anuncio

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['id', 'Nome', 'Site', 'Instagram', 'Responsavel', 'Telefone_do_Responsavel']


class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = ['id', 'Nome_do_Anuncio', 'Data_Inicial', 'Data_Final', 'Valor_do_Anuncio', 'Anexos', 'Tempo_do_Anuncio', 'Codigo_da_Empresa']
        