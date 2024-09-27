import logging
from backend.clickhouse_connection import connect_to_clickhouse


def fetch_clickhouse_metrics():
    """Fetches telemetry metrics from ClickHouse."""
    try:
        logging.info("Fetching metrics from ClickHouse...")
        client = connect_to_clickhouse()
        query = "SELECT * FROM system.dashboards WHERE title ILIKE '%CPU%'"
        result = client.query(query)
        logging.info("Data fetched from ClickHouse.")
        return result.result_rows
    except Exception as e:
        logging.error(f"Error fetching data from ClickHouse: {e}")
        raise
