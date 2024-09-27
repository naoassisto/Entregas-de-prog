import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go

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

# Mapping technical metric names to user-friendly labels
metric_labels = {
    "MemoryTracking": "Memory Usage (Bytes)",
    "QueryThread": "Active Query Threads",
    "TCPConnection": "TCP Connections",
    "OpenFileForRead": "Open Files for Read",
    "ZooKeeperSession": "ZooKeeper Sessions",
    "ZooKeeperWatch": "ZooKeeper Watches"
}

# Function to fetch system metrics and filter out zero values
def fetch_system_metrics():
    query = """
    SELECT 
        metric, 
        value 
    FROM system.metrics
    """
    data = query_clickhouse(query)
    if not data:
        return pd.DataFrame()  # Return an empty DataFrame if there's no data

    # Convert the result into a pandas DataFrame and filter out rows with zero values
    df = pd.DataFrame(data, columns=['metric', 'value'])
    df = df[df['value'] != 0]  # Filter out zero values

    # Replace metric names with friendly labels
    df['metric'] = df['metric'].replace(metric_labels)
    
    return df

# Function to visualize system metrics
def visualize_system_metrics():
    st.markdown("### System Metrics Overview")
    system_metrics = fetch_system_metrics()

    if not system_metrics.empty:
        st.write("Displaying only metrics with non-zero values:")
        st.table(system_metrics)  # Display the system metrics in a table format

        # Visualize key metrics in a bar chart
        fig = go.Figure([go.Bar(x=system_metrics['metric'], y=system_metrics['value'])])
        fig.update_layout(title='System Metrics', xaxis_title='Metric', yaxis_title='Value', template='plotly_dark')
        st.plotly_chart(fig)
    else:
        st.write("No system metrics data found.")

# Function to visualize memory usage and active query threads
def visualize_memory_threads():
    query = """
    SELECT 
        value AS memory_usage
    FROM system.metrics
    WHERE metric = 'MemoryTracking'
    """
    memory_data = query_clickhouse(query)

    query = """
    SELECT 
        value AS query_threads
    FROM system.metrics
    WHERE metric = 'QueryThread'
    """
    thread_data = query_clickhouse(query)

    if memory_data and thread_data:
        memory_df = pd.DataFrame(memory_data, columns=['memory_usage'])
        thread_df = pd.DataFrame(thread_data, columns=['query_threads'])

        # Create a bar chart showing memory usage and active query threads
        fig = go.Figure()
        fig.add_trace(go.Bar(x=['Memory Usage'], y=memory_df['memory_usage'], name='Memory Usage', marker_color='rgb(158,202,225)', textposition='auto'))
        fig.add_trace(go.Bar(x=['Active Query Threads'], y=thread_df['query_threads'], name='Active Query Threads', marker_color='rgb(255,182,193)', textposition='auto'))
        fig.update_layout(title='Memory Usage and Active Query Threads', xaxis_title='Metric', yaxis_title='Value', template='plotly_dark')
        st.plotly_chart(fig)
    else:
        st.write("No memory or thread data available.")

# Function to visualize active TCP connections
def visualize_tcp_connections():
    query = """
    SELECT 
        value AS tcp_connections
    FROM system.metrics
    WHERE metric = 'TCPConnection'
    """
    data = query_clickhouse(query)

    if data:
        df = pd.DataFrame(data, columns=['tcp_connections'])

        # Create a bar chart showing active TCP connections
        fig = go.Figure([go.Bar(x=['TCP Connections'], y=df['tcp_connections'], marker_color='rgb(255,165,0)')])
        fig.update_layout(title='Active TCP Connections', xaxis_title='Metric', yaxis_title='Connections', template='plotly_dark')
        st.plotly_chart(fig)
    else:
        st.write("No TCP connection data available.")

# Main Telemetry Dashboard
st.title("📊 **ClickHouse Dashboard Telemetria**")

# Adding sidebar for navigation and filters
st.sidebar.title("Filter Data")
time_range = st.sidebar.selectbox("Select Time Range", ["Last 24 hours", "Last 7 days", "Last 30 days"])

# Tabbed layout for better organization
tab1, tab2, tab3 = st.tabs(["🔍 System Metrics", "🧠 Memory and Threads", "🌐 TCP Connections"])

# Visualize system metrics with improved aesthetics in the first tab
with tab1:
    st.markdown("## System Metrics Overview")
    visualize_system_metrics()

# Visualize memory usage and active query threads in the second tab
with tab2:
    st.markdown("## Memory Usage and Active Query Threads")
    visualize_memory_threads()

# Visualize active TCP connections in the third tab
with tab3:
    st.markdown("## Active TCP Connections")
    visualize_tcp_connections()

