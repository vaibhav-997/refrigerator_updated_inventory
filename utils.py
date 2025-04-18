import qrcode
from io import BytesIO
import datetime
import streamlit as st

def generate_qr(product_name, lot_number, expiry_date):
    """Generate a QR code containing product details including expiry date."""
    qr_data = f"Product: {product_name}\nLot: {lot_number}\nExpiry: {expiry_date}"
    qr = qrcode.make(qr_data)
    qr_bytes = BytesIO()
    qr.save(qr_bytes, format="PNG")
    return qr_bytes.getvalue()



# style.py
import streamlit as st

def hide_sidebar():
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            [data-testid="stSidebar"] {display: none;}
            [data-testid="collapsedControl"] {display: none;}
        </style>
    """, unsafe_allow_html=True)


def navbar():
    st.markdown(
        """
        <style>
        .navbar {
            display: flex;
            justify-content: space-around;
            padding: 10px;
            background-color: #0078D4;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .navbar a {
            text-decoration: none;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
        }
        .navbar a:hover {
            background-color: #005A8C;
        }
        </style>
        <div class="navbar">
            <a href="http://localhost:8501" target="_self">Home</a>
            <a href="http://localhost:8501/Product_Regsitratin" target="_self">Register Product</a>
            <a href="http://localhost:8501/Products" target="_self">View Products</a>
            <a href="http://localhost:8501/Update_Delete" target="_self">Update/Delete</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
