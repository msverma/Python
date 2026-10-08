#Implement a program that reads a CSV file and generates a bar chart to represent the data using Matplotlib2

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("📊 Sales Performance Dashboard (GitHub CSV)")

# GitHub raw CSV link
csv_url = "https://raw.githubusercontent.com/msverma/Python/f5b1c37e646f49f686d04fe892232193734e2604/Sales_performance.csv"


# Read CSV directly from GitHub
df = pd.read_csv(csv_url)
st.write("Data Preview:", df.head())



#df.head()
if {'CategoryName','Quantity','Sales'}.issubset(df.columns):
    df['TotalSales']=df['Quantity']*df['Sales']
    category_sales= df.groupby('CategoryName')['TotalSales'].sum()
    #print (category_sales)
    #plot bar chart
    fig, ax = plt.subplots(figsize=(8,6))
    
    category_sales.plot(kind='bar',color='skyblue', edgecolor='black',ax=ax)
    ax.set_title("📊 Category-wise Total Sales Revenue")
    ax.set_xlabel("Category")
    ax.set_ylabel("Total Revenue")
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    st.error("CSV must contain 'CategoryName', 'Quantity', and 'Sales' columns")


