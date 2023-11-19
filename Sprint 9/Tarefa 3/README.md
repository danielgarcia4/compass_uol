# Sprint 9

## Tarefa: Desafio Parte 3 - Processamento da Trusted

### Job para processamento dos arquivos CSV

![job csv](img/01.png)

* Script

``` python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

schema = StructType([
    StructField("id", StringType(), True),
    StructField("tituloPrincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", IntegerType(), True),
    StructField("tempoMinutos", IntegerType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", DoubleType(), True),
    StructField("numeroVotos", IntegerType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", IntegerType(), True),
    StructField("anoFalecimento", IntegerType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True)
])

movies_csv_raw = 's3://desafio-1-compass/Raw/Local/CSV/Movies/2023/10/25/movies.csv'

raw_data1 = spark.read.csv(movies_csv_raw, header=True, schema=schema, sep="|")
raw_data1.write.mode("overwrite").parquet('s3://desafio-3-compass/Trusted/CSV/Parquet/')

job.commit()
```

* Job details

![job details](img/02.png)

![job details](img/03.png)

* Run

![run job](img/04.png)

* Arquivos no bucket do S3

![estrutura de pastas](img/05.png)

![arquivos parquet](img/06.png)

![arquivos parquet](img/07.png)


### Job para processamento dos arquivos JSON

![job json](img/08.png)

* Script

``` python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import StructType, StructField, IntegerType, BooleanType, StringType, DoubleType, DateType
from pyspark.sql.functions import lit

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

json_schema = StructType([
    StructField("Id", IntegerType(), True),
    StructField("Adulto", BooleanType(), True),
    StructField("Idioma original", StringType(), True),
    StructField("Popularidade", DoubleType(), True),
    StructField("Data de lançamento", DateType(), True)
])

tmdb_s3_path = "s3://desafio-1-compass/Raw/TMDB/JSON/2023/11/04/"

dt = '2023-11-04'

tmdb_data = spark.read.json(tmdb_s3_path, schema=json_schema)

tmdb_data = tmdb_data.withColumn("dt", lit(dt))

tmdb_data.write.mode("overwrite").partitionBy("dt").parquet("s3://desafio-3-compass/Trusted/TMDB/Parquet")

job.commit()

```

* Job details

![job details](img/09.png)

![job details](img/10.png)

* Run

![run job](img/11.png)

* Arquivos no bucket do S3

![estrutura de pastas](img/12.png)

![arquivos parquet](img/13.png)

![arquivos parquet](img/14.png)


### Criação das Tabelas referentes aos arquivos CSV

* Criação da Crawler

Para a criação das tabelas, resolvi usar as Crawlers, pois eles monitoram nosso armazenamento de dados de
modo a criar e atualizar metadados no Glue de forma automática, logo criam a tabela automaticamente.


![crawler MoviesTrustedCrawler](img/15.png)

![crawler MoviesTrustedCrawler](img/16.png)

**Obs:** Aproveitei a role IAM criada no laboratório AWS Glue (da Sprint 7), pois ela já associa as politícas necessárias (AmazonS3FullAccess, AWSLakeFormationDataAdmin, AWSGlueConsoleFullAccess e
CloudWatchFullAccess), permitindo o acesso do Glue ao S3.

* Crawler Run

![crawler run](img/17.png)

* Consulta da tabela no Athena

![visão geral e query](img/18.png)

![tabela](img/19.png)

![tabela](img/20.png)

![resultado](img/21.png)


### Criação das Tabelas referentes aos arquivos JSON


* Crawler

![crawler MoviesTmdbTrusted](img/22.png)

* Crawler Run

![crawler run](img/23.png)

* Consulta da tabela no Athena

![tabela e query](img/24.png)

![tabela e query](img/25.png)


