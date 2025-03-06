import kafka import KafkaProducer
import json
import requests
import time

producer = KafkaProducer(bootstrap_server = "localhost:9092", value_serializer = lambda v: json.dumps(v).encode("utf-8"))

API_URL = "https://api.example.com/stock_prices"

def fetch_stock_prices():
    response = requests.get(API_URL)
    return response.json()
    
def publish_stock_data():
    while True:
        stock_data = fetch_stock_prices()
        producer.send("stock_prices", stock_data)
        print(f"Published: {stock_data}")
        time.sleep(60)
        
if __name__ == "__main__":
    publish_stock_data()
