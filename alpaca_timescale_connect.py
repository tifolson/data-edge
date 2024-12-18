import asyncio
import asyncpg
from alpaca.data.live import StockDataStream
from alpaca.data.models import Bar
from functools import partial
import config_file


# Define your Alpaca API credentials
ALPACA_API_KEY = config_file.API_KEY
ALPACA_SECRET_KEY = config_file.API_SECRET


# Define your Timescale connection
CONNECTION = config_file.URL


# Function to handle incoming data and insert it into TimescaleDB
async def handle_message(msg, conn):
    print(f"Received message: {msg}")

    if isinstance(msg, Bar):  # Check if the message is a bar
        symbol = msg.symbol
        timestamp = msg.timestamp
        open_price = msg.open
        high_price = msg.high
        low_price = msg.low
        close_price = msg.close
        volume = msg.volume
        trade_count = msg.trade_count
        vwap = msg.vwap


        # Print formatted bar data
        print(f"--- Bar Data ---")
        print(f"Symbol: {symbol}")
        print(f"Timestamp: {timestamp}")
        print(f"Open: {open_price}")
        print(f"High: {high_price}")
        print(f"Low: {low_price}")
        print(f"Close: {close_price}")
        print(f"Volume: {volume}")
        print(f"Trade Count: {trade_count}")
        print(f"Vwap: {vwap}")
        print("-----------------")


        # Insert the bar data into TimescaleDB
        query = """
        INSERT INTO streaming_test (symbol, timestamp, open, high, low, close, volume, trade_count, vwap)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
        """

        await conn.execute(query,
                           symbol,
                           timestamp,
                           open_price,
                           high_price,
                           low_price,
                           close_price,
                           volume,
                           trade_count,
                           vwap
                           )
    else:
        print("Received non-bar message:", msg)

# Function to start the WebSocket stream
async def start_stream():
    conn = await asyncpg.connect(CONNECTION)
    print("Connected to TimescaleDB.")

    stream = StockDataStream(ALPACA_API_KEY, ALPACA_SECRET_KEY)
    print("Created StockDataStream instance.")

    # Use functools.partial to pass the connection to the handler
    handler = partial(handle_message, conn=conn)

    # Subscribe to bar data for a specific stock (e.g.,TSLA)
    stream.subscribe_bars(handler, 'TSLA')

    print("Subscribed to TSLA bars. Starting stream...")

    await stream._run_forever()  # Use the internal coroutine directly


# Run the WebSocket stream
loop = asyncio.get_event_loop()
loop.run_until_complete(start_stream())
