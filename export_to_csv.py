import psycopg2
import pandas as pd

DB_CONFIG = {
    "dbname": "stock_data",
    "user": "your_user",
    "password": "your_password",
    "host": "your-db-instance.rds.amazonaws.com",
    "port": "5432"
}

conn = psycopg2.connect(**DB_CONFIG)
query = " SELECT * FROM stock_prices"
df = pd.read_sql(query,conn)
df.to_csv(stock_prices.csv", index = False)
conn.close()
print("Exported stock_prices.csv)
