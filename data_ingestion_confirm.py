import asyncpg
import asyncio
import config_file

# Connection string for TimescaleDB
CONNECTION = config_file.URL

async def fetch_data():
    conn = await asyncpg.connect(CONNECTION)
    print("Connected to TimescaleDB.")

    query = "SELECT * FROM streaming_test LIMIT 10;"
    rows = await conn.fetch(query)

    for row in rows:
        print(row)

    await conn.close()
    print("Connection closed.")


loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_data())