import streamlit as st
import pandas as pd

from analytics import clean_data, generate_kpis, correlation_matrix
from charts import plot_numeric_columns
from ai_agent import generate_ai_insights

st.title("AI-Powered Analytics Dashboard")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data")
    st.write(df.head())

    df = clean_data(df)

    st.subheader("Cleaned Data")
    st.write(df.head())

    kpis = generate_kpis(df)

    st.subheader("KPIs")
    st.write(kpis)

    corr = correlation_matrix(df)

    st.subheader("Correlation Matrix")
    st.write(corr)

    st.subheader("Charts")
    plot_numeric_columns(df)

    if st.button("Generate AI Insights"):

        insights = generate_ai_insights(kpis, corr)

        st.subheader("AI Insights")
        st.write(insights)

    st.divider() 
    st.subheader("Chat with your Data")

    user_question = st.text_input("Ask a specific question about your data (e.g., 'Which month is best?')")

    if user_question:
        with st.spinner("Thinking..."):
            answer = generate_ai_insights(kpis, f"User Question: {user_question}")
            st.write(f"**AI Answer:** {answer}")



    st.divider()
    st.subheader("Export Analysis")

    
    if 'insights' in locals():
        import os
        if not os.path.exists("reports"):
            os.makedirs("reports")
            
        with open("reports/report.txt", "w") as f:
            f.write(insights)

        st.download_button(
            label="Download AI Analysis Report",
            data=insights,
            file_name="business_report.txt",
            mime="text/plain"
        )
    else:
        st.info("Generate AI Insights above to enable report download.")
