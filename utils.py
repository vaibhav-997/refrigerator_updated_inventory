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



