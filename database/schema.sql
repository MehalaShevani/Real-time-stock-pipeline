CREATE TABLE stock_prices (
	id SERIAL PRIMARY KEY,
	timestamp TIMESTAMP NOT NULL,
	symbol VARCHAR(10) NOT NULL,
	price FLOAT NOT NULL);
