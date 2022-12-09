## Requisitos

- [Docker](https://www.docker.com)

- [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

- [Django](https://www.djangoproject.com)

- [Zappa](https://github.com/zappa/Zappa)

- [PostgreSQL](https://www.postgresql.org)

## Serviços utilizados:

- [ElephantSQL](https://www.elephantsql.com)
- [AWS Lambda](https://aws.amazon.com/pt/lambda/)
- [AWS S3 Bucket](https://aws.amazon.com/pt/s3/)

## Instalação

Inicie o docker, clone o repositório e entre na pasta

```bash
git clone https://github.com/macdev14/edesoft.git master
cd edesoft

```
## Imagem Docker

Monte a imagem através do comando
```bash
docker build -t empirica-docker-image . 
```
Pode executar através de duas maneiras

- Script para Windows


```bash
 empiricashell.bat
```
- Script para Mac OS
```bash
 source empiricashell.sh
```
- Manualmente
```docker
 docker run -ti -p 8000:8000 -v "$(pwd):/var/task" -v ~/.aws/:/root/.aws  --rm empirica-docker-image
```

## Imagem em Execução
 - Criar e ativar o Ambiente Virtual
```bash
 virtualenv ve
 source ve/bin/activate
```

- Instalar pacotes python
```python
 pip install -r requirements.txt
```

- Escrever no banco de dados
```python
 python manage.py makemigrations
 python manage.py migrate
```



## Variaveis de Ambiente

- Configurar chaves AWS
```bash
 aws configure
```
- Configurar Banco de Dados e AWS
```bash
echo -e "\nDATABASE_URL={sua_uri_do_bancodedados}" >> .env
echo -e "\nAWS_ACCESS_KEY_ID={sua_aws_access_key}" >> .env
echo -e "\nAWS_SECRET_ACCESS_KEY_ID={sua_aws_secret_access_key}" >> .env
echo -e "\nAWS_STORAGE_BUCKET_NAME={nome_do_buckets3}" >> .env
```
# Criar evento e associar  a código lambda
- Iniciar o zappa
```bash
zappa init

```

## Configurar o Zappa e Adicionar Eventos - zappa_settings.json
[Saiba Mais](https://github.com/zappa/Zappa#executing-in-response-to-aws-events)

- Colocar sua função em 
```json 
events:[
    { 
     function: "sua_função"
    }
]
```
- Quando deve ser acionada em 
```json 
events:[
{ 
   event_source:
   { 
        "events": ["tipos_de_eventos_aws"], 
   }
}
]
```

- Filtrar tipo de arquivo
```json
"key_filters": [
     { 
           "type": "suffix",
           "value": ".csv"
     }
]
```

```json
{
    "dev": {
        "aws_region": "sa-east-1",
        "django_settings": "core.settings",
        "profile_name": "zappa",
        "project_name": "task",
        "runtime": "python3.8",
        "s3_bucket": "zappa-971hba1vj",
        "events": [
            {
              "function": "core.events.lambda_handler",
              "event_source": {
                "arn": "arn:aws:s3:::zappa-971hba1vj",
                "batch_size": 10,
                "enabled": true,
                "events": ["s3:ObjectCreated:*","s3:ObjectAcl:Put"],
                "key_filters": [{ 
                    "type": "suffix",
                    "value": ".csv"
                  }]
              }
            }
          ]


    }
}

```

## Criar evento e enviar para o lambda

```bash
zappa deploy <nome_de_stage>
#exemplo
zappa deploy dev

```

## Atualizar evento/código e enviar para o lambda

```bash
zappa update <nome_de_stage>
#exemplo
zappa update dev
```



## Licença

[MIT](https://choosealicense.com/licenses/mit/)