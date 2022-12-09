# Generated by Django 4.1.3 on 2022-12-05 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CessaoFundo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originador', models.CharField(max_length=250)),
                ('doc_originador', models.CharField(max_length=250)),
                ('cedente', models.CharField(max_length=250)),
                ('doc_cedente', models.IntegerField()),
                ('ccb', models.IntegerField()),
                ('id_externo', models.IntegerField()),
                ('cliente', models.CharField(max_length=250)),
                ('cpf_cnpj', models.CharField(max_length=250)),
                ('endereco', models.CharField(max_length=250)),
                ('cep', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=250)),
                ('uf', models.CharField(max_length=50)),
                ('valor_do_emprestimo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_parcela', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_parcelas', models.IntegerField()),
                ('parcela', models.IntegerField()),
                ('data_de_emissao', models.DateField()),
                ('data_de_vencimento', models.DateField()),
                ('preco_de_aquisicao', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
