import streamlit as st
import datetime
from database import insert_product

st.title("📌 Register New Product")

# Form Inputs
name = st.text_input("Product Name")
lot_number = st.text_input("Lot Number")
mfg_date = st.date_input("Manufacture Date", datetime.date.today())
expiry_date = st.date_input("Expiry Date", datetime.date.today())
category = st.selectbox("Category", ["Cold Bottle", "Ice Cream", "Dairy Products", "Medical Products"])

if st.button("Register Product"):
    if insert_product(name, lot_number, mfg_date, expiry_date, category):
        st.success("✅ Product Registered Successfully!")
        st.rerun()
    else:
        st.error("❌ Error registering product!")
