import psycopg2

DB_CONFIG = {
    "dbname": "stock_data",
    "user": "your_user",
    "password": "your_password",
    "host": "your-db-instance.rds.amazonaws.com",
    "port": "5432"
}

def get_db_connection():
    """Establish a connection to teh PostgreSQL database"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
