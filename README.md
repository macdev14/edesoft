## Requirements

- [Docker](https://www.docker.com)

- [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

- [Django](https://www.djangoproject.com)

- [Zappa](https://github.com/zappa/Zappa)

- [PostgreSQL](https://www.postgresql.org)

## Services used:

- [ElephantSQL](https://www.elephantsql.com)
- [AWS Lambda](https://aws.amazon.com/pt/lambda/)
- [AWS S3 Bucket](https://aws.amazon.com/pt/s3/)

## Installation

Start docker, clone the repository and enter the folder

```bash
git clone https://github.com/macdev14/edesoft.git master
edesoft cd

```
## Docker Image

Mount the image using the command
```bash
docker build -t empirica-docker-image .
```
Can run through two ways

- Script for Windows


```bash
  empiricashell.bat
```
- Script for Mac OS
```bash
  source empiricashell.sh
```
- Manually
```docker
  docker run -ti -p 8000:8000 -v "$(pwd):/var/task" -v ~/.aws/:/root/.aws --rm empirica-docker-image
```

## Running Image
  - Create and activate the Virtual Environment
```bash
  virtualenv see
  source ve/bin/activate
```

- Install python packages
```python
  pip install -r requirements.txt
```




## Environment variables

- Configure Database, AWS and secret key
```bash
echo -e '''SECRET_KEY=your_secret_key''' >> .env
echo -e '''DATABASE_URL=your_database_uri''' >> .env
echo -e '''AWS_ACCESS_KEY_ID=your_aws_access_key''' >> .env
echo -e '''AWS_SECRET_ACCESS_KEY_ID=your_aws_secret_access_key''' >> .env
echo -e '''AWS_STORAGE_BUCKET_NAME=bucket_name_s3''' >> .env
echo -e '''AWS_S3_REGION_NAME=bucket_region''' >> .env
```

## Configure database and collect static files
```python
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py collectstatic
```


# Create event and associate with lambda code
- Start zappa
```bash
zappa init

```



## Configure Zappa and Add Events - zappa_settings.json
[Learn More](https://github.com/zappa/Zappa#executing-in-response-to-aws-events)

- Put your role in
```json
events:[
     {
      function: "your_function"
     }
]
```
- When should it be activated in
```json
events:[
{
    event_source:
    {
         "events": ["aws_event_types"],
    }
}
]
```

- Filter file type
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

## Create event and send to lambda

```bash
zappa deploy <stage_name>
#example
zappa deploy dev

```

## Update event/code and send to lambda

```bash
zappa update <stage_name>
#example
zappa update dev
```



## License

[MIT](https://choosealicense.com/licenses/mit/)
