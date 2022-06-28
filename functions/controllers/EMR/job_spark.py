from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

#Esse código foi realizado via Step Job no AWS EMR.

'''
Para utilizar este job, na criação do Step utilizar os seguintes argumentos:
 - Jar location: command-runner.jar
 - Arguments: spark-submit --master yarn --deploy-mode cluster s3://pathway_to_your_job_code
'''


spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter",";")
    .load("s3://datalake-enem2020-vinisiq/data/")
)

(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .save("s3://datalake-enem2020-vinisiq/data/staging/enem")
)