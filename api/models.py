from django.db import models

# Create your models here.
class CessaoFundo(models.Model):

    originador = models.CharField(max_length=250)
    doc_originador = models.CharField(max_length=250)
    cedente = models.CharField(max_length=250)
    doc_cedente = models.BigIntegerField(default=0)
    ccb = models.BigIntegerField(default=0)
    id_externo = models.BigIntegerField(default=0)
    cliente = models.CharField(max_length=250)
    cpf_cnpj = models.CharField(max_length=250)
    endereco = models.CharField(max_length=250)
    cep = models.CharField(max_length=50)
    cidade = models.CharField(max_length=250)
    uf = models.CharField(max_length=50)
    valor_do_emprestimo = models.DecimalField(max_digits=10,decimal_places=2)
    valor_parcela = models.DecimalField(max_digits=10,decimal_places=2)
    total_parcelas = models.BigIntegerField(default=0)
    parcela = models.BigIntegerField(default=0)
    data_de_emissao = models.DateField()
    data_de_vencimento = models.DateField()
    preco_de_aquisicao = models.DecimalField(max_digits=10,decimal_places=2)
    

