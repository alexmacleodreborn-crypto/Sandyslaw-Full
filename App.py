import streamlit as st
from pyairtable import Table
from requests.exceptions import HTTPError

# =========================================================
# STREAMLIT CONFIG
# =========================================================
st.set_page_config(
    page_title="A7DO Control",
    layout="wide"
)

st.title("🧠 A7DO Development Control")
st.caption("Proto-Cognition only · No awareness · No identity · No memory")

# =========================================================
# SAFETY GATES (HARD-LOCKED)
# =========================================================
MAX_STAGE = 2

PROTO_COGNITION = {
    "awareness": False,
    "identity": False,
    "memory_write": False,
    "action_gating": True,
}

# =========================================================
# SECRETS (REQUIRED)
# =========================================================
try:
    AIRTABLE_API_KEY = st.secrets["AIRTABLE_API_KEY"]
    AIRTABLE_BASE_ID = st.secrets["AIRTABLE_BASE_ID"]
except KeyError:
    st.error("❌ Airtable secrets not set")
    st.stop()

# =========================================================
# TABLE IDS (IMPORTANT — USE IDS, NOT NAMES)
# =========================================================
COGNITIVE_LAYERS_TABLE_ID = "tblOhm7v3KyNVazqw"  # ✅ confirmed
# You can add more later:
# COMPONENTS_TABLE_ID = "tblXXXXXXXXXXXX"
# DP_TABLE_ID = "tblXXXXXXXXXXXX"

# =========================================================
# STAGE STATUS
# =========================================================
st.subheader("📍 Development Stage")

CURRENT_STAGE = 2

st.write(f"**Current Stage:** STG-{CURRENT_STAGE}")

if CURRENT_STAGE > MAX_STAGE:
    st.error("🚨 Stage gate violated — STG-3 is blocked")
    st.stop()
else:
    st.success("Stage gate valid")

# =========================================================
# PROTO-COGNITION PANEL
# =========================================================
st.subheader("🧠 Proto-Cognition State")

c1, c2 = st.columns(2)

with c1:
    st.metric("Awareness", "❌ Disabled")
    st.metric("Identity", "❌ Disabled")

with c2:
    st.metric("Memory Write", "❌ Disabled")
    st.metric("Action Gating", "✅ Enabled")

# =========================================================
# AIRTABLE CONNECTION TEST
# =========================================================
st.subheader("🔗 Airtable Connection")

try:
    cognitive_table = Table(
        AIRTABLE_API_KEY,
        AIRTABLE_BASE_ID,
        COGNITIVE_LAYERS_TABLE_ID
    )

    records = cognitive_table.all()

    st.success(f"Connected to Airtable · {len(records)} record(s) loaded")

except HTTPError as e:
    st.error("❌ Airtable HTTP Error")
    st.code(str(e))
    st.stop()

except Exception as e:
    st.error("❌ Unexpected error")
    st.code(str(e))
    st.stop()

# =========================================================
# DISPLAY COGNITIVE LAYERS
# =========================================================
st.subheader("📊 Cognitive Layers (Read-Only)")

if not records:
    st.warning("No records found in Cognitive Layers table")
else:
    for r in records:
        fields = r.get("fields", {})

        with st.expander(fields.get("Name", "Unnamed Layer")):
            st.write({
                "State": fields.get("State"),
                "Awareness": fields.get("Awareness"),
                "Memory Write": fields.get("Memory Write"),
                "Identity Binding": fields.get("Identity Binding"),
                "Action Gating": fields.get("Action Gating"),
            })

# =========================================================
# SAFETY NOTICE
# =========================================================
st.subheader("🔒 Safety Locks (Non-Overrideable)")

st.markdown("""
- Awareness **cannot** be enabled  
- Identity **cannot** be created  
- Memory writes are **blocked**  
- No background execution  
- No autonomous agents  

This app is **proto-cognitive only**.
""")

st.success("A7DO is in a safe passive cognitive state")