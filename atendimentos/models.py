from django.db import models
from cidade.models import Estado, Cidade, Area
from formulario.models import TipoOs, TipoContato, GrupoProblema, DescricaoProblema, TipoSolucao, CodCancelamento

class Atendimento(models.Model):
    num_contrato = models.IntegerField()
    num_os = models.IntegerField()
    node = models.CharField(max_length=64)
    tipo_os = models.ForeignKey(TipoOs, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    tipo_contato = models.ForeignKey(TipoContato, on_delete=models.CASCADE)
    mac_adress = models.CharField(max_length=128)
    modelo_equipamento = models.CharField(max_length=128)
    reclamacao_cliente = models.TextField()
    grupo_problema = models.ForeignKey(GrupoProblema, on_delete=models.CASCADE)
    descricao_problema = models.ForeignKey(DescricaoProblema, on_delete=models.CASCADE)    
    tipo_solucao = models.ForeignKey(TipoSolucao, on_delete=models.CASCADE)
    cod_cancelamento = models.ForeignKey(CodCancelamento, on_delete=models.CASCADE)
    observacao = models.TextField()

    def __str__(self) -> str:
        return str(self.num_contrato)
