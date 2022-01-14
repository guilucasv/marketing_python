from django.db import models

class Empresa(models.Model):
    Nome = models.CharField(max_length=50)
    Site = models.URLField(max_length=100)
    Instagram = models.URLField(max_length=100)
    Responsavel = models.CharField(max_length=50)
    Telefone_do_Responsavel = models.CharField(max_length=50)

    def __str__(self):
        return self.Nome

class Anuncio(models.Model):
    Nome_do_Anuncio = models.CharField(max_length=50)
    Data_Inicial = models.DateField()
    Data_Final = models.DateField()
    Valor_do_Anuncio = models.FloatField(max_length=50)
    Anexos = models.FileField(upload_to="C:/Users/lucas.silva/Documents/APP_MARKETING/imagens")
    Tempo_do_Anuncio = models.PositiveIntegerField()
    Codigo_da_Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nome_do_Anuncio