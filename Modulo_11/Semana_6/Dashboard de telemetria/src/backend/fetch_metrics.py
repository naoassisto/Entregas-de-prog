import logging
from backend.clickhouse_connection import connect_to_clickhouse


def fetch_clickhouse_metrics():
    """Fetches basic metrics from ClickHouse."""
    try:
        logging.info("Fetching basic metrics from ClickHouse...")
        client = connect_to_clickhouse()

        # Run a simple query like getting the version of the ClickHouse server
        query = "SELECT version()"
        result = client.query(query)

        logging.info("Data fetched from ClickHouse.")
        return result.result_rows
    except Exception as e:
        logging.error(f"Error fetching data from ClickHouse: {e}")
        raise

