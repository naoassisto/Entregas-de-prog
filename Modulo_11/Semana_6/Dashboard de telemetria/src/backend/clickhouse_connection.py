import os
import logging
from clickhouse_connect import get_client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def connect_to_clickhouse():
    """Connects to ClickHouse using the HTTP interface."""
    # Strip environment variables to remove any leading/trailing spaces
    clickhouse_host = os.getenv("CLICKHOUSE_HOST").strip()
    clickhouse_port = os.getenv("CLICKHOUSE_PORT").strip()
    clickhouse_user = os.getenv("CLICKHOUSE_USER").strip()
    clickhouse_password = os.getenv("CLICKHOUSE_PASSWORD").strip()
    clickhouse_db = os.getenv("CLICKHOUSE_DB").strip()

    # Check for missing environment variables
    if not all([clickhouse_host, clickhouse_port, clickhouse_user, clickhouse_password, clickhouse_db]):
        raise ValueError("Missing required ClickHouse environment variables.")

    try:
        # Increase the timeout value and apply additional settings
        client = get_client(
            interface='http',  # Use HTTP interface
            host=clickhouse_host,
            port=int(clickhouse_port),
            username=clickhouse_user,
            password=clickhouse_password,
            database=clickhouse_db,
            secure=True,  # Ensure HTTPS
            verify=False,  # Disable SSL verification for testing
            connect_timeout=60000  # Increased timeout (in milliseconds)
        )
        logging.info(f"Connected to ClickHouse using HTTP: {clickhouse_host}:{clickhouse_port}")
        return client
    except Exception as e:
        logging.error(f"Error connecting to ClickHouse: {e}")
        raise

def fetch_clickhouse_metrics():
    """Fetches metrics from ClickHouse."""
    try:
        logging.info("Fetching metrics from ClickHouse...")
        client = connect_to_clickhouse()
        query = "SELECT * FROM metrics_table"
        result = client.query(query)
        logging.info("Data fetched from ClickHouse.")
        return result.result_rows
    except Exception as e:
        logging.error(f"Error fetching data from ClickHouse: {e}")
        raise

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        data = fetch_clickhouse_metrics()
        logging.info(f"Fetched data: {data}")
    except Exception as e:
        logging.error(f"Failed to fetch data: {e}")
