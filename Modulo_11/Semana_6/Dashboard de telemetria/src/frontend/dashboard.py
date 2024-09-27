import streamlit as st
import pandas as pd
import requests

# Base URL for the Flask API
FLASK_API_URL = "http://localhost:5000"

# Function to query ClickHouse via Flask API
def query_clickhouse(query):
    try:
        response = requests.post(f"{FLASK_API_URL}/clickhouse/query", json={"query": query})
        if response.status_code == 200:
            return response.json()  # Assuming the data is returned in JSON format
        else:
            st.error(f"Error querying ClickHouse: {response.json().get('error')}")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"Connection error: {e}")
        return []

# Function to fetch ClickHouse metrics data
def fetch_clickhouse_metrics():
    query = """
    SELECT 
        query_id, 
        query, 
        formatReadableTimeDelta(query_duration_ms) AS query_duration 
    FROM system.query_log 
    WHERE (type != 'QueryStart') 
    ORDER BY event_time DESC 
    LIMIT 10
    """
    data = query_clickhouse(query)
    if not data:
        return pd.DataFrame()  # Return an empty DataFrame if there's no data

    # Convert the result into a pandas DataFrame
    df = pd.DataFrame(data, columns=['query_id', 'query', 'query_duration'])
    return df

# Streamlit app code
st.title("ClickHouse Telemetry Dashboard")

st.write("Fetching metrics from ClickHouse...")

try:
    # Fetching metrics data using the Flask API
    metrics_data = fetch_clickhouse_metrics()
    if not metrics_data.empty:
        st.write("Fetched metrics data:")
        st.table(metrics_data)  # Display the data as a table
    else:
        st.write("No metrics data found.")
except Exception as e:
    st.error(f"Failed to fetch data: {e}")
