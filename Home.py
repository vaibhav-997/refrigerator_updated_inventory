import streamlit as st

st.title("Manage your regfrigerator inventory along with the expiry")

# with st.sidebar:
#     st.markdown("### 📌 Navigation")
#     st.page_link("pages/1_Product_Registration.py", label="📝 Register Product")
#     st.page_link("pages/2_Products.py", label="📂 View Products")
#     st.page_link("pages/3_Update_Delete.py", label="✏️ Update/Delete Products")

# # Initialize session state for login
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# # User authentication (Replace with actual logic)
# def login():
#     st.title("🔐 Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
    
#     if st.button("Login"):
#         if username == "admin" and password == "password":  # Replace with real auth
#             st.session_state.logged_in = True
#             st.rerun()
#         else:
#             st.error("Invalid credentials")

# # Logout function
# def logout():
#     st.session_state.logged_in = False
#     st.rerun()

# # **Only show navigation after login**
# if not st.session_state.logged_in:
#     login()  # Show login page
# else:
#     # **Show Sidebar Navigation after login**
#     with st.sidebar:
#         st.markdown("### 📌 Navigation")
#         st.page_link("pages/1_Product_Registration.py", label="📝 Register Product")
#         st.page_link("pages/2_Products.py", label="📂 View Products")
#         st.page_link("pages/3_Update_Delete.py", label="✏️ Update/Delete Products")
#         st.button("🚪 Logout", on_click=logout)
