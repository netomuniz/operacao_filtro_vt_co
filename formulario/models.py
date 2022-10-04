from django.db import models

class TipoOs(models.Model):
    tipo_os = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.tipo_os
        

class TipoContato(models.Model):
    tipo_contato = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.tipo_contato


class GrupoProblema(models.Model):
    grupo_problema = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.grupo_problema


class DescricaoProblema(models.Model):
    grupo_problema = models.ForeignKey(GrupoProblema, on_delete=models.CASCADE)
    descricao_problema = models.CharField(max_length=100)    

    def __str__(self) -> str:
        return self.descricao_problema


class TipoSolucao(models.Model):
    tipo_solucao = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.tipo_solucao
        

class CodCancelamento(models.Model):
    cod_cancelamento = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.cod_cancelamento