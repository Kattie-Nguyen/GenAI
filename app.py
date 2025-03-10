# app.py

import streamlit as st
from chatbot import (
    get_total_revenue, get_net_income_change, get_total_assets,
    get_total_liabilities, get_cash_flow, get_revenue_change,
    get_asset_change, get_liabilities_change, get_cash_flow_change
)

# Streamlit App Layout
st.title("📊 Financial Analysis Chatbot")

st.markdown("""
Welcome to the Financial Insights Chatbot for **Microsoft**, **Tesla**, and **Apple** for fiscal years 2022–2024.

You can ask about the following:

- Total Revenue  
- Revenue Change (%)  
- Net Income Change (%)  
- Total Assets  
- Asset Change (%)  
- Total Liabilities  
- Liabilities Change (%)  
- Cash Flow from Operating Activities  
- Cash Flow Change (%)

#### 💬 Example Questions:
- What is the total revenue for Microsoft?  
- How has net income changed for Tesla?  
- What are the total assets of Apple?  
- What is the liabilities change for Tesla?  
- What is the cash flow change for Microsoft?
""")

# User Input
user_query = st.text_input("💬 Ask your financial question:")

# Define list of supported companies
companies = ['Microsoft', 'Tesla', 'Apple']

# Chatbot Logic
if user_query:
    user_query = user_query.lower()
    matched_company = None

    for company in companies:
        if company.lower() in user_query:
            matched_company = company
            break

    if matched_company:
        if "total revenue" in user_query:
            st.subheader(f"📈 Total Revenue for {matched_company}")
            st.write(get_total_revenue(matched_company))

        elif "revenue change" in user_query:
            st.subheader(f"📊 Revenue Change (%) for {matched_company}")
            st.write(get_revenue_change(matched_company))

        elif "net income change" in user_query:
            st.subheader(f"💸 Net Income Change (%) for {matched_company}")
            st.write(get_net_income_change(matched_company))

        elif "total assets" in user_query:
            st.subheader(f"🏢 Total Assets for {matched_company}")
            st.write(get_total_assets(matched_company))

        elif "asset change" in user_query:
            st.subheader(f"📊 Asset Change (%) for {matched_company}")
            st.write(get_asset_change(matched_company))

        elif "total liabilities" in user_query:
            st.subheader(f"📉 Total Liabilities for {matched_company}")
            st.write(get_total_liabilities(matched_company))

        elif "liabilities change" in user_query:
            st.subheader(f"📊 Liabilities Change (%) for {matched_company}")
            st.write(get_liabilities_change(matched_company))

        elif "cash flow change" in user_query:
            st.subheader(f"💹 Cash Flow Change (%) from Operating Activities for {matched_company}")
            st.write(get_cash_flow_change(matched_company))

        elif "cash flow" in user_query:
            st.subheader(f"💵 Cash Flow from Operating Activities for {matched_company}")
            st.write(get_cash_flow(matched_company))

        else:
            st.warning("⚠️ Sorry, I couldn't understand your query. Try rephrasing it.")
    else:
        st.warning("⚠️ Please include one of the supported companies: Microsoft, Tesla, or Apple.")
