import streamlit as st
from streamlit_option_menu import option_menu

# Hide the default sidebar and Streamlit's top header
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        header[data-testid="stHeader"] {
            display: none;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Navbar using option_menu
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

# Home content
if selected == "Home":
    st.title("Manage your Refrigerator Inventory Along with the Expiry")
    st.markdown("""
        This app allows you to register products,  
        view products by category, and update or delete product details,  
        including expiry dates.
    """)
