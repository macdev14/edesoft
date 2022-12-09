import datetime
import boto3, json, urllib.parse
import pandas as pd
import sys
import csv, io, re
from api.models import CessaoFundo
from decimal import Decimal

s3_client = boto3.client("s3")
S3_BUCKET = 'BUCKET_NAME'


if sys.version_info[0] < 3: 
    from StringIO import StringIO # Python 2.x
else:
    from io import StringIO # Python 3.x

s3 = boto3.client('s3')


def lambda_handler(event, context):
    print('called')
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)['Body'].read()
        doc = pd.read_csv(io.BytesIO(response), delimiter=';', encoding='latin1')
        r = doc.iterrows()
        objs  = [
            CessaoFundo(
                originador=row['Originador'],
                doc_originador=row['Doc Originador'],
                cedente=row['Cedente'],
                doc_cedente=row['Doc Cedente'],
                ccb=int(row['CCB']),
                id_externo=int(row['Id']),
                cliente=row['Cliente'],
                cpf_cnpj=row['CPF/CNPJ'],
                endereco=row['Endereço'],
                cep=row['CEP'],
                cidade=row['Cidade'],
                uf=row['UF'],
                valor_do_emprestimo= float('.'.join(re.findall(r"[-+]?\d*\.\d+|\d+", str(row['Valor do Empréstimo'])))),
                valor_parcela=float('.'.join(re.findall(r"[-+]?\d*\.\d+|\d+", str(row['Parcela R$']) ) ) ),
                total_parcelas=int(row['Total Parcelas']),
                parcela=int(row['Parcela #']),
                data_de_emissao=datetime.datetime.strptime(row['Data de Emissão'], "%d/%m/%Y").date(),
                data_de_vencimento= datetime.datetime.strptime(row['Data de Vencimento'], "%d/%m/%Y").date() ,
                preco_de_aquisicao= float('.'.join(re.findall(r"[-+]?\d*\.\d+|\d+", str(row['Preço de Aquisição']) ) ) )  


            )
            
            for index, row in r
        ]
        CessaoFundo.objects.bulk_create(objs)

        
        return response
    except Exception as e:
        print("ERROR")
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
 