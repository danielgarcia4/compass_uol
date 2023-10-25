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