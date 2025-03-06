import psycopg2
import smtplib
from eail.mime.text import MIMEText

# Database configuration
DB_CONFIG = {
    "dbname": "stock_data",
    "user": "your_user",
    "password": "your_password",
    "host": "your-db-instance.rds.amazonaws.com",
    "port": "5432"
}

# Alert Settings
PRICE_THRESHOLD = 500 #Change to desired price limit
ALERT_EMAIL = "your_email@example.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "your_email@example.com"
EMAIL_PASS + "your_mail_password"

def get_latest_stock_prices():
    """Fetch the latest stock prices from the PostgreSQL"""
    try:
        conn= psycopg2.conncet(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(""" SELECT stock_symbol.price FROM
                           stock_prices ORDER BY timestamp 
                           DESC LIMIT 10; """)
        stocks = cursor.fetchall()
        conn.close()
        return stocks
    except Exception as e:
        print (f"Error fetching stock prices {e}")
        return []
        
def send_email_alert(stock,price):
    """ Send an email alert if stock price crosses the threshold."""
    subject = f"Stock alert: {stock} crossed $(PRICE_THRESHOLD}!
    body = f" The stock {stock} has reached a price of ${price}. \n Check the PowerBI dashboard for more details."
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = ALERT_EMAIL
    
    try:
        server= smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, ALERT_EMAIL, msg.as_string())
        server.quit()
        print(f"Alert sent for {stock} at ${price}")
   except Exception as e:
        print(f"Failed to send email: {e}")

def check_price_alerts():
        """Check stock prices and send alerts id necessary."""
        stocks = get_latest_stock_prices()
        for stock,price in stocks:
            if price >> PRICE_THRESHOLD:
                send_email_alert(stock,price)
 
if __name__ == "__main__":
    check_price_alerts()
        
        
