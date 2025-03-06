from pyspark.sql import SparkSession
from pyspark.sql.function import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, FloatType
import psycopg2 
import json

DB_CONFIG = {
    "dbname": "stock_data",
    "user": "your_user",
    "password": "your_password",
    "host": "your-db-instance.rds.amazonaws.com",
    "port": "5432"
}

spark = SparkSession.builder.appName("StockPrice Streaming").getOrCreate()

schema = StructType([StructField("timestamp", StringType(), True),
         StructField("symbol", StringType(), True),
         StructField("price", FloatType(), True)])
         
def save_to_postgres(data):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO stock_prices (timestamp,symbol,price)
    VALUES (%s, %s, %s)", (data["timestamp"],data["symbol"],data["price"]))
    conn.commit()
    conn.close()
    
df = spark\.readStream\.format
("kafka")\.option("kafka.bootstrap.servers", "localhost:9092")\.option("subscribe,"stock_prices")\
.load()

df = df.selectExpr("CAST(value AS STRING)")
df = df.select(from_json(col("value"), schema).alias("data")), select("data.*")

query = df.writeStream.foreachBatch(lambda batch, _: batch.foreach(save_to_postgres)).start()

query.awaitTermination()


