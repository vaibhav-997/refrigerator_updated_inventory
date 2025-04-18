import streamlit as st
from database import fetch_all_products, display_products
from utils import hide_sidebar, navbar
from streamlit_option_menu import option_menu

hide_sidebar()
# Custom Navbar Function
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

st.title("🗂️ Product Categories")

# Fetch products from DB
products = fetch_all_products()

# Check for expired products
from datetime import datetime
def check_expired_products():
    today = datetime.date( datetime.today())
    expired = []
    expiring_soon = []

    for product in products:
        expire_date = product.get("expire")
        if expire_date:
            try:
                expire_date = datetime.strptime(expire_date, "%Y-%m-%d").date()
                days_left = (expire_date - today).days

                if days_left < 0:  
                    expired.append(product)
                elif days_left <= 7:  
                    expiring_soon.append(product)

            except ValueError:
                st.error(f"❌ Invalid Date Format for {product['ProductName']}")

    # 🔴 Show Expired Products
    if expired:
        st.error("🚨 **Expired Products:**")
        for p in expired:
            st.write(f"❌ `{p['ProductName']}` (Lot: {p['LotNumber']}) **expired on {p['expire']}**")

    # 🟡 Show Products Expiring Soon
    if expiring_soon:
        st.warning("⚠️ **Products Expiring Soon (within 7 days):**")
        for p in expiring_soon:
            st.write(f"🕒 `{p['ProductName']}` (Lot: {p['LotNumber']}) **expires on {p['expire']}**")

check_expired_products()

# Display filtered products
display_products(products)
