import base64
import streamlit as st
import pandas as pd
import base64

import mysql.connector
from utils import generate_qr

# Database configuration
DB_CONFIG = {
    "host": "82.180.143.66",
    "user": "u263681140_students",
    "password": "testStudents@123",
    "database": "u263681140_students",
}

def connect_db():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        st.error(f"Database connection failed: {e}")
        return None



def display_products(products):
    st.title("All Registered Products")

    if not products:
        st.warning("No products found in the database.")
        return

    # Prepare data for table
    table_data = []
    for product in products:
        product_name = product.get("ProductName", "N/A")
        lot_number = product.get("LotNumber", "N/A")
        manufacture_date = product.get("Mfg", "N/A")  
        expiry_date = product.get("expire", "N/A")  # Ensure correct column name
        category = product.get("Category", "N/A")
        
        # Debugging: Print product details (optional)
        # st.write("Product Data:", product)

        # Create a downloadable link for QR Code
        qr_code_data = product.get("QRCode")
        if qr_code_data:
            b64 = base64.b64encode(qr_code_data).decode()  # Encode as Base64
            href = f'<a href="data:image/png;base64,{b64}" download="QR_{lot_number}.png">Download</a>'
        else:
            href = "No QR Code"

        # Append product details along with the download link
        table_data.append([product_name, lot_number, category, manufacture_date, expiry_date, href])

    # Create DataFrame for table
    df = pd.DataFrame(table_data, columns=["Product Name", "Lot Number", "Category", "Manufacture Date", "Expiry Date", "Download QR Code"])

    # Display table with HTML rendering for download links
    st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)


def fetch_all_products():
    
    conn = connect_db()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, ProductName, LotNumber,QRCode,Category, Mfg, COALESCE(expire, '0000-00-00') AS expire FROM Enventry ORDER BY id DESC"
        )
        results = cursor.fetchall()
        conn.close()
        return results
    return []


def insert_product(name, lot_number, mfg, expiry, category):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        qr_code = generate_qr(name, lot_number, expiry)
        try:
            cursor.execute(
                "INSERT INTO Enventry (ProductName, LotNumber, Mfg, Expire, Category, QRCode) VALUES (%s, %s, %s, %s, %s, %s)",
                (name, lot_number, mfg, expiry, category, qr_code),
            )
            conn.commit()
            return True
        except mysql.connector.Error as e:
            st.error(f"Error inserting data: {e}")
        finally:
            conn.close()
    return False

# Function to update a product (with new QR Code)
import mysql.connector
from database import connect_db
from utils import generate_qr

def update_product(product_id, new_name, new_lot, category, new_mfg, new_expire):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()

        # Generate new QR Code
        qr_code = generate_qr(new_name, new_lot, new_expire)

        try:
            cursor.execute(
                """
                UPDATE Enventry 
                SET ProductName = %s, LotNumber = %s, Mfg = %s, expire = %s, QRCode = %s, Category = %s
                WHERE id = %s
                """,
                (new_name, new_lot, new_mfg, new_expire, qr_code, category, product_id),
            )
            conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error updating product: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

# Function to delete a product
def delete_product(product_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Enventry WHERE id = %s", (product_id,))
            conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error deleting product: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
            
def fetch_products_by_category(category):
    """Fetch products based on the selected category."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)
    
    if category == "All":
        cursor.execute("SELECT * FROM Enventry ORDER BY id DESC")
    else:
        cursor.execute("SELECT * FROM Enventry WHERE Category = %s ORDER BY id DESC", (category,))
    
    results = cursor.fetchall()
    conn.close()
    return results