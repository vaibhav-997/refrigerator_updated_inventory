import streamlit as st
from database import fetch_all_products, update_product, delete_product
import qrcode
from io import BytesIO
from datetime import datetime

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

        # Ensure dates are properly formatted
        mfg_date = datetime.strptime(product_data["Mfg"], "%Y-%m-%d").date() if isinstance(product_data["Mfg"], str) else product_data["Mfg"]
        exp_date = datetime.strptime(product_data["expire"], "%Y-%m-%d").date() if isinstance(product_data["expire"], str) else product_data["expire"]

        # Pre-fill form with existing values
        new_name = st.text_input("Product Name", value=product_data["ProductName"])
        new_lot = st.text_input("Lot Number", value=product_data["LotNumber"])
        new_mfg = st.date_input("Manufacture Date", value=mfg_date)
        new_expire = st.date_input("Expiry Date", value=exp_date)  # Fixed key usage
        category_options = ["Cold Bottle", "Cold Items", "Ice Cream", "Dairy Products", "Medical Products"]
        category = st.selectbox("Category", category_options, index=category_options.index(product_data["Category"]))

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

