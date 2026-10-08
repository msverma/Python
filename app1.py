import pandas as pd
import streamlit as st

st.title("📊 Sales Performance Dashboard")

# Upload CSV file
file = st.file_uploader("Upload Sales CSV file", type=["csv"])

if file is not None:
    df = pd.read_csv(file)
    st.write("Data Preview:", df.head())

    # Select category
    if {"CategoryName", "Quantity", "Sales"}.issubset(df.columns):
        category_name = st.selectbox("Select Category", df["CategoryName"].unique())

        product_cat = df[df["CategoryName"] == category_name]
        total_sales = (product_cat["Quantity"] * product_cat["Sales"]).sum()

        st.success(f"Category: {category_name} → Total Sales: {round(total_sales,2)}")
    else:
        st.error("CSV must contain 'CategoryName', 'Quantity', and 'Sales' columns")
