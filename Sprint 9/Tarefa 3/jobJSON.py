import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from awsglue.context import DynamicFrame

# @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

tmdb_s3_path = "s3://desafio-1-compass/Raw/TMDB/JSON/2023/11/21/"

spark_df = spark.read.json(tmdb_s3_path)

spark_df.write.format('parquet').mode("overwrite").save("s3://desafio-3-compass/Trusted/TMDB/Parquet")

job.commit()