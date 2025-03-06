Real-Time Stock Pipeline Tracker with Kafka, Spark & PostgreSQL

A real-time stock market data pipeline using Apache Kafka, Apache Spark and PostgreSQL with PowerBI for visualization.

Overview:

This project streams real-time stock price data from an external API using Kafka, processes it with Spark and stores it in a PostgreSQL database for analysis. 
The data is then visualized using Power BI dashboards to moniter stock trends.

Tech Stack:

Kafka --> Real-time streaming
Spark --> Data processing
PostgreSQL --> Data storage
Power BI --> Data visualization
AWS EC2, RDS --> Cloud deployment

How to Run?

1. Start Kafka & Spark
2. Run producer.py --> Fetch & send stock data to Kafka
3. Run consumer.py --> Read from Kafka & save to PostgreSQL
4. Connect Power BI to to PostgreSQL
5. Visualize insights and trends

Setup & Installation

Prerequisites
 -> Python 3.xinstalled
 -> Kafka & Spark installed (or use Docker)
 -> PostgreSQL database set up

Step 1: Clone the repository:

git clone
https://github.com/your-username/real-time-stock-pipeline.git
cd real-time-stock-pipeline

Step 2: Set Up PostgreSQL database

* Create a PostgreSQL database (stock_data)
*  Run the SQL script to create the table:

psql -U your_user -d stock_data -f database/schema.sql

Step 3: Install dependencies

pip install -r kafka_producer/requirements.txt
pip install -r spark_consumer/requirements.txt
pip install -r scripts/requirements.txt

Step 4: Running the Pipeline

-> Start Kafka & Spark
docker-compose up -d
-> Start the Kafka Producer
python kafka_producer/producer.py (To fetch live stock prices and sends them to kafka)
-> Start the Spark consumer
python spark_consumer/consumer.py (To read stock prices from Kafka and write to PostgreSQL)
-> Export data for Power BI
python scripts/export_to_csv.py (To generate stock_prices.csv for Power BI visualization)

Step 5: Power BI Dashboard

1. Open powerbi/report.pbix in Power BI.
2. Connect to PostgreSQL or import stock_prices.csv.
3. View real-time stock price trends, comparisons and insights.

Step 6: Cloud Deployment

Deploying on AWS
* PostgreSQL -> Host on AWS RDS
* Kafka & Spark -> Deploy on AWS EC2
* Power BI -> Conncet to AWS RDS 


