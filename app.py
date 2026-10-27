import streamlit as st
from db import init_db
from staff_profile import render_staff_profile_form
from admin_panel import render_admin_panel

st.set_page_config(page_title="HRIS Management System", layout="wide")

# Initialize database table if not exists
init_db()

menu = st.sidebar.selectbox(
    "Navigation Menu", 
    ["📋 Staff Form", "🛡️ Admin / Management Panel"]
)

if menu == "📋 Staff Form":
    render_staff_profile_form()
elif menu == "🛡️ Admin / Management Panel":
    render_admin_panel()