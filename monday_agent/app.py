import streamlit as st
from monday_api import get_board_items
from data_cleaning import convert_to_dataframe
from agent import interpret_query
from business_logic import compute_pipeline

# YOUR REAL BOARD IDs
DEALS_BOARD_ID = 5026932277
WORK_ORDERS_BOARD_ID = 5026934474

st.title("Monday.com Business Intelligence Agent")

question = st.text_input("Ask a business question:")

if question:

    st.write("### 🧠 Interpreting Question")
    intent = interpret_query(question)
    st.json(intent)

    # Decide which board to fetch
    if intent["board_required"].lower() == "deals":
        board_id = DEALS_BOARD_ID
    elif intent["board_required"].lower() == "work_orders":
        board_id = WORK_ORDERS_BOARD_ID
    else:
        board_id = DEALS_BOARD_ID  # default fallback

    st.write("### 📡 Live API Call")
    st.code(f"Fetching board ID: {board_id}")

    response = get_board_items(board_id)

    df = convert_to_dataframe(response)

    st.write("### 📊 Data Preview")
    st.dataframe(df.head())

    if intent["metric"].lower() == "pipeline":
        result = compute_pipeline(df, intent["sector"])
        st.write("### 📈 Business Insights")
        st.json(result)