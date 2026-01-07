import streamlit as st

st.set_page_config(page_title="Ryndex", layout="wide")

st.title("Ryndex")
st.caption("Vending performance insights by industry & ZIP code")

st.divider()

# --- Inputs ---
col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    industry = st.selectbox(
        "Industry",
        ["Gym", "Office", "Manufacturing", "Healthcare", "Education", "Other"],
        index=0,
    )

with col2:
    zipcode = st.text_input("ZIP code", value="37209", max_chars=5)

with col3:
    run = st.button("Run", type="primary")

# --- Output ---
st.divider()
st.subheader("Top Products")

if run:
    st.info("Placeholder results (next step: connect BigQuery).")
    st.dataframe(
        [
            {"product": "Protein Bar", "units": 120, "revenue": 420.00, "avg_price": 3.50},
            {"product": "Energy Drink", "units": 95, "revenue": 380.00, "avg_price": 4.00},
            {"product": "Electrolyte Water", "units": 60, "revenue": 180.00, "avg_price": 3.00},
        ],
        use_container_width=True,
    )
else:
    st.write("Choose an industry + ZIP code, then click **Run**.")
