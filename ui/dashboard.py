import requests
import streamlit as st
import pandas as pd

API_BASE = "https://agentops-7lsn.onrender.com"

st.set_page_config(page_title="AgentOps Dashboard", layout="wide")
st.title("📊 AgentOps – Autonomous BI Dashboard")
st.caption("Live multi-agent analytics with memory, ML & adaptive reasoning")

# ---------------------------
# Load system state
# ---------------------------
resp = requests.get(f"{API_BASE}/dashboard/state")

if resp.status_code != 200:
    st.error("Backend not reachable")
    st.stop()

state = resp.json()

# ---------------------------
# Top-level metrics
# ---------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("System Mode", state["system_mode"])
col2.metric("Memory Size", state["memory_size"])
col3.metric(
    "Recent Anomalies",
    state["recent_memory_analysis"]["recent_anomalies"]
)
col4.metric(
    "Severity",
    state["recent_memory_analysis"]["severity"].upper()
)

# ---------------------------
# Adaptive thresholds
# ---------------------------
st.subheader("⚙ Adaptive Thresholds")

thr = state["adaptive_thresholds"]

st.json(thr)

# ---------------------------
# Recent Events Table
# ---------------------------
# ---------------------------
# Recent Events Table
# ---------------------------
st.subheader("📜 Recent Events")

events = state["last_events"]

if events:
    rows = []
    for e in events:
        rows.append({
            "Query": e["query"],
            "Anomaly": e["anomaly"]["anomaly"],
            "Severity": e["anomaly"]["severity"],
            "Forecast": e["forecast"]["forecast_next_period"],
            "Actions": ", ".join(e["actions"]),
            "Time": e["timestamp"]
        })

    df = pd.DataFrame(rows)
    st.dataframe(df, width="stretch")
else:
    st.info("No events recorded yet")

# ---------------------------
# Manual refresh
# ---------------------------
if st.button("🔄 Refresh"):
    st.rerun()

if st.button("▶ Run demo query"):
    requests.post(
        f"{API_BASE}/query",
        json={"user_query": "why did revenue drop"}
    )
    st.success("Demo query executed. Refreshing dashboard…")
