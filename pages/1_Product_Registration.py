import streamlit as st 
import datetime
from database import insert_product
from utils import hide_sidebar, navbar
from streamlit_option_menu import option_menu

hide_sidebar()

selected = option_menu(
    menu_title=None,
    options=["Home", "Register Product", "View Products", "Update/Delete"],
    icons=["house", "plus-square", "card-list", "pencil-square"],
    orientation="horizontal",
    # styles={
    #     "container": {"padding": "0!important", "background-color": "#2c7be5"},
    #     "nav-link": {
    #         "font-size": "16px",
    #         "color": "white",
    #         "margin": "0 10px",
    #         "padding": "10px 20px",
    #         "transition": "0.3s"
    #     },
    #     "nav-link-selected": {"background-color": "#1b5ab6"},
    # }
)

# Navigation logic
if selected == "Register Product":
    st.switch_page("pages/1_Product_Registration.py")
elif selected == "View Products":
    st.switch_page("pages/2_Products.py")
elif selected == "Update/Delete":
    st.switch_page("pages/3_Update_Delete.py")



# Calling navbar function to display at the top
# navbar()

st.title("📌 Register New Product")

# Form Inputs
name = st.text_input("Product Name")
lot_number = st.text_input("Lot Number")
mfg_date = st.date_input("Manufacture Date", datetime.date.today())
expiry_date = st.date_input("Expiry Date", datetime.date.today())
category = st.selectbox("Category", ["Cold Bottle", "Ice Cream", "Dairy Products", "Medical Products","Masale","Snacks"])

if st.button("Register Product"):
    if insert_product(name, lot_number, mfg_date, expiry_date, category):
        st.success("✅ Product Registered Successfully!")
        st.rerun()
    else:
        st.error("❌ Error registering product!")

