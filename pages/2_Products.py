import streamlit as st
from database import fetch_all_products, display_products


st.title("🗂️ Product Categories")

# Fetch products from DB
products = fetch_all_products()

# Check for expired products
from datetime import datetime
def check_expired_products():
    today = datetime.date( datetime.today())
    products = fetch_all_products()

    expired = []
    expiring_soon = []

    for product in products:
        expire_date = product.get("expire")  # Ensure key matches DB
        if expire_date:
            try:
                expire_date = datetime.strptime(expire_date, "%Y-%m-%d").date()
                days_left = (expire_date - today).days

                if days_left < 0:  # Already expired
                    expired.append(product)
                elif days_left <= 7:  # Expiring in next 7 days
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

# Define available categories
categories = ["All", "Cold Bottle", "Ice Cream", "Dairy Products", "Medical Products"]
selected_category = st.selectbox("Select a category", categories)

# Filter products based on category
if selected_category != "All":
    products = [p for p in products if p["Category"] == selected_category]

# Display filtered products
display_products(products)  # ✅ Pass the filtered list
