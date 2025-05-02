import streamlit as st
from database import fetch_all_products, update_product, delete_product
import qrcode
from io import BytesIO
from datetime import datetime

from utils import hide_sidebar, navbar
from streamlit_option_menu import option_menu

hide_sidebar()

# Custom Navbar Function
selected = option_menu(
    menu_title=None,
    options=["Home", "Register Product", "View Products", "Update/Delete"],
    icons=["house", "plus-square", "card-list", "pencil-square"],
    orientation="horizontal",
)

# Navigation logic
if selected == "Register Product":
    st.switch_page("pages/1_Product_Registration.py")
elif selected == "View Products":
    st.switch_page("pages/2_Products.py")
elif selected == "Update/Delete":
    st.switch_page("pages/3_Update_Delete.py")

# Title
st.title("✏️ Update/Delete Products")

# Fetch all products
products = fetch_all_products()

if products:
    product_options = {f"{p['ProductName']} (Lot: {p['LotNumber']})": p["id"] for p in products}
    selected_product = st.selectbox("Select Product", list(product_options.keys()))

    if selected_product:
        product_id = product_options[selected_product]

        # Get the existing values
        product_data = next(p for p in products if p["id"] == product_id)

        # Pre-fill form with existing values
        new_name = st.text_input("Product Name", value=product_data["ProductName"])
        new_lot = st.text_input("Lot Number", value=product_data["LotNumber"])
        new_mfg = st.date_input("Manufacture Date", value=datetime.strptime(product_data["Mfg"], "%Y-%m-%d").date())
        new_expire = st.date_input("Expiry Date", value=datetime.strptime(product_data["expire"], "%Y-%m-%d").date())

        category_options = ["Cold Bottle", "Ice Cream", "Dairy Products", "Medical Products"]

        # Handle unknown or missing category gracefully
        if product_data["Category"] not in category_options:
            category_options.insert(0, product_data["Category"])  # Add it at the top
        default_index = category_options.index(product_data["Category"])

        category = st.selectbox("Category", category_options, index=default_index)

        if st.button("Update Product"):
            # Generate new QR Code
            qr_data = f"{new_name} - {new_lot} - Expiry: {new_expire}"
            qr = qrcode.make(qr_data)
            qr_bytes = BytesIO()
            qr.save(qr_bytes, format="PNG")
            qr_code_data = qr_bytes.getvalue()

            # Update the product in the database
            success = update_product(product_id, new_name, new_lot, category, str(new_mfg), str(new_expire))
            if success:
                st.success("✅ Product updated successfully! New QR Code generated.")
                st.rerun()
            else:
                st.error("❌ Failed to update product!")

        if st.button("Delete Product"):
            success = delete_product(product_id)
            if success:
                st.warning("🚨 Product deleted successfully!")
                st.rerun()
            else:
                st.error("❌ Failed to delete product!")
else:
    st.info("ℹ️ No products available to update or delete.")
