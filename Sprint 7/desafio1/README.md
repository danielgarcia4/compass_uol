# Sprint 7

## Desafio - Parte 1

### 1) Implementar código Python:

* script.py

``` python
import boto3
from datetime import datetime

# Configuração AWS
chave_acesso = 'AKIA5NRJIXPBPPADD2M6'
chave_acesso_secreta = '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'
s3 = boto3.client('s3', aws_access_key_id=chave_acesso, aws_secret_access_key=chave_acesso_secreta)

# Arquivos CSV
movies = 'movies.csv'
series = 'series.csv'

# Caminho do bucket
nome_bucket = 'desafio-1-compass'
camada_armazenamento = 'Raw'
origem_dado = 'Local'
formato_dado = 'CSV'
data_processamento = datetime.now().strftime('%Y/%m/%d')
caminho_movies = f'{camada_armazenamento}/{origem_dado}/{formato_dado}/Movies/{data_processamento}/{movies}'
caminho_series = f'{camada_armazenamento}/{origem_dado}/{formato_dado}/Series/{data_processamento}/{series}'

# Gravação no S3
s3.upload_file(movies, nome_bucket, caminho_movies)
s3.upload_file(series, nome_bucket, caminho_series)
```

### 2) Criar container Docker com um volume para armazenar os arquivos CSV e executar processo Python implementado

* Dockerfile

``` dockerfile
FROM python:3.8

WORKDIR /app

COPY script.py .
COPY movies.csv .
COPY series.csv .

RUN pip install boto3

CMD ["python", "script.py"]
```

* Criação da imagem

![criação da imagem](./img/1.png)

### 3) Executar localmente o container docker para realizar a carga dos dados ao S3

* Criando e executando container

![execução container](./img/2.png)

### Arquivos criados no S3

* movies.csv

![movies.csv no bucket](./img/4.png)

* series.csv

![series.csv no bucket](./img/3.png)
