import sys
import os

# Add the src folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import streamlit as st
from backend.fetch_metrics import fetch_clickhouse_metrics


st.title("ClickHouse Telemetry Dashboard")

st.write("Fetching metrics from ClickHouse...")

try:
    data = fetch_clickhouse_metrics()
    st.write("Fetched metrics data:")
    st.table(data)
except Exception as e:
    st.error(f"Failed to fetch data: {e}")
