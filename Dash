import streamlit as st
from pyairtable import Table

# -----------------------
# CONFIG
# -----------------------
st.set_page_config(page_title="A7DO Control", layout="wide")

AIRTABLE_API_KEY = st.secrets.get("AIRTABLE_API_KEY", "")
AIRTABLE_BASE_ID = st.secrets.get("AIRTABLE_BASE_ID", "")

# Example table names
COGNITIVE_TABLE = "Cognitive Layers"
COMPONENTS_TABLE = "Components"

# -----------------------
# SAFETY GATES (HARD)
# -----------------------
MAX_STAGE = 2

PROTO_COGNITION = {
    "awareness": False,
    "identity": False,
    "memory_write": False,
    "action_gating": True
}

# -----------------------
# UI
# -----------------------
st.title("🧠 A7DO Development Control")

st.markdown("""
**Proto-Cognition Enabled**  
Awareness, identity, and memory are **disabled by design**.
""")

# -----------------------
# STAGE STATUS
# -----------------------
current_stage = 2
st.subheader("📍 Development Stage")

st.write(f"**Current Stage:** STG-{current_stage}")

if current_stage > MAX_STAGE:
    st.error("Stage gate violated. STG-3 is blocked.")
    st.stop()

st.success("Stage gate valid")

# -----------------------
# PROTO-COGNITION PANEL
# -----------------------
st.subheader("🧠 Proto-Cognition State")

col1, col2 = st.columns(2)

with col1:
    st.metric("Awareness", "❌ Disabled")
    st.metric("Identity", "❌ Disabled")

with col2:
    st.metric("Memory Write", "❌ Disabled")
    st.metric("Action Gating", "✅ Enabled")

# -----------------------
# OPTIONAL: AIRTABLE READ
# -----------------------
if AIRTABLE_API_KEY and AIRTABLE_BASE_ID:
    st.subheader("📊 Cognitive Layers (Airtable)")
    table = Table(AIRTABLE_API_KEY, AIRTABLE_BASE_ID, COGNITIVE_TABLE)
    records = table.all()

    for r in records:
        st.write({
            "Layer": r["fields"].get("Name"),
            "State": r["fields"].get("State"),
            "Awareness": r["fields"].get("Awareness"),
            "Memory": r["fields"].get("Memory Write"),
        })
else:
    st.info("Airtable not connected yet.")

# -----------------------
# HARD BLOCK
# -----------------------
st.subheader("🔒 Safety Locks")

st.write("""
- Awareness cannot be enabled here  
- Identity cannot be created  
- Memory writes are blocked  
""")
