# Data Edge: Real-Time Database Management System

## Project Overview

Data Edge is a Python-based system designed to ingest live data points and build a timestamp-focused database of said data.

### Key Features

- **Live Data Ingestion**: Captures real-time financial market data. Bars, trades (ticks), and quotes are available for stocks, options on stocks, and crypto.
- **Dynamic Database Management**: Stores and updates information.

## Websocket communication between Alpaca and TimescaleDB
This is a method for ingesting live financial market data from Alpaca Market's data API and storing it in a relational database hosted on AWS by way of TimescaleDB.
It functions by calling the desired data from Alpaca and placing it in a PostgreSql database using TimescaleDB, a wrapper that prioritizes time.


### Prerequisites
- Python 3.8+
- Required Libraries:
  ```
  pip install -r requirements.txt
  ```
- Alpaca market data subscription
  - Sign up for free to get API keys.
- TimescaleDB subscription
  - Sign up for free to get API keys.

##Limitations and Considerations:
- This is a research project used for identifying bottlenecks and managing data between multiple API owners.
- Timescale has a free 30-day trial. Sign up for free to get API keys and test the API for yourself.
  [TimescaleDB 30-Day Free Trial](https://console.cloud.timescale.com/signup)


## Data Information
- Alpaca has free data that is delayed by 15 minutes. For live data, a paid subscription is required. 

Source: [Alpaca Historical Option Data Documentation](https://docs.alpaca.markets/docs/historical-option-data#:~:text=Indicative%20Pricing%20Feed%20is%20a,re%20delayed%20by%2015%20minutes.&text=OPRA%20is%20the%20consolidated%20BBO%20feed%20of%20OPRA.)  
Source: [Alpaca Historical Stock Data Documentation](https://docs.alpaca.markets/docs/historical-stock-data-1)

## License
Apache 2.0

## Disclaimer
This tool is for informational purposes only. Tick data is subject to change at any time due to corruption, incorrect trade information, and data provider outages. Not financial advice. Use responsibly.

---

**Contact**: tifanieoriley@gmail.com



  
