import matplotlib.pyplot as plt
import streamlit as st


def plot_numeric_columns(df):
    numeric_cols = df.select_dtypes(include='number').columns

    for col in numeric_cols:
        fig, ax = plt.subplots()
        ax.hist(df[col], bins=20)
        ax.set_title(f"Distribution of {col}")
        st.pyplot(fig)