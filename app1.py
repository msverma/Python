import pandas as pd
import streamlit as st

st.title("📊 Sales Performance Dashboard")

# Upload CSV file
file = st.file_uploader("Upload Sales CSV file", type=["csv"])

if file is not None:
    df = pd.read_csv(file)
    st.write("Data Preview:", df.head())

    # Check required columns
    if {"CategoryName", "Quantity", "Sales"}.issubset(df.columns):
        # Select category
        category_name = st.selectbox("Select Category", df["CategoryName"].unique())

        product_cat = df[df["CategoryName"] == category_name]
        total_sales = (product_cat["Quantity"] * product_cat["Sales"]).sum()

        st.success(f"Category: {category_name} → Total Sales: {round(total_sales,2)}")

        # 🔥 Bar chart for all categories
        df["Revenue"] = df["Quantity"] * df["Sales"]
        category_sales = df.groupby("CategoryName")["Revenue"].sum().reset_index()

        st.subheader("📈 Category-wise Total Sales")
        st.bar_chart(category_sales.set_index("CategoryName"))
    else:
        st.error("CSV must contain 'CategoryName', 'Quantity', and 'Sales' columns")

