import streamlit as st
import sqlite3
import pandas as pd
import os

st.set_page_config(page_title="Admin Panel", layout="wide")
st.title("🛡️ HRIS Admin & Governance Panel")

def get_connection():
    return sqlite3.connect("hris.db")

conn = get_connection()

# Password protection in sidebar
admin_passcode = st.sidebar.text_input("Admin Access Key", type="password")
if admin_passcode != "admin123":
    st.warning("🔒 Please enter a valid Admin Access Key in the sidebar.")
    st.stop()

st.success("Access Granted — Administrator Mode Active")

# Admin tabs
admin_tab1, admin_tab2, admin_tab3 = st.tabs([
    "🌴 Leave Approvals", 
    "🛒 Procurement Approvals", 
    "⚙️ Database Tools"
])

# --- 1. LEAVE APPROVALS ---
with admin_tab1:
    st.subheader("Pending Leave Requests")
    try:
        pending_leaves = pd.read_sql_query("""
            SELECT l.id, e.name as Employee, l.leave_type, l.start_date, l.end_date, l.status 
            FROM leave_requests l 
            JOIN employees e ON l.employee_id = e.id 
            WHERE l.status = 'Pending'
        """, conn)
    except Exception:
        pending_leaves = pd.DataFrame()

    if not pending_leaves.empty:
        for _, row in pending_leaves.iterrows():
            c1, c2, c3 = st.columns([4, 1, 1])
            c1.write(f"**{row['Employee']}** — {row['leave_type']} ({row['start_date']} to {row['end_date']})")
            if c2.button("✅ Approve", key=f"app_{row['id']}"):
                cursor = conn.cursor()
                cursor.execute("UPDATE leave_requests SET status = 'Approved' WHERE id = ?", (row['id'],))
                conn.commit()
                st.rerun()
            if c3.button("❌ Decline", key=f"dec_{row['id']}"):
                cursor = conn.cursor()
                cursor.execute("UPDATE leave_requests SET status = 'Declined' WHERE id = ?", (row['id'],))
                conn.commit()
                st.rerun()
    else:
        st.info("No pending leave requests.")

# --- 2. PROCUREMENT APPROVALS ---
with admin_tab2:
    st.subheader("Pending Procurement Approvals")
    try:
        pending_proc = pd.read_sql_query("""
            SELECT p.id, e.name as Requester, p.item_description, p.estimated_cost, p.status 
            FROM procurement p 
            JOIN employees e ON p.requested_by = e.id 
            WHERE p.status = 'Pending'
        """, conn)
    except Exception:
        pending_proc = pd.DataFrame()

    if not pending_proc.empty:
        for _, row in pending_proc.iterrows():
            c1, c2, c3 = st.columns([4, 1, 1])
            c1.write(f"**{row['Requester']}** — {row['item_description']} (${row['estimated_cost']:,.2f})")
            if c2.button("✅ Approve", key=f"app_proc_{row['id']}"):
                cursor = conn.cursor()
                cursor.execute("UPDATE procurement SET status = 'Approved' WHERE id = ?", (row['id'],))
                conn.commit()
                st.rerun()
            if c3.button("❌ Decline", key=f"dec_proc_{row['id']}"):
                cursor = conn.cursor()
                cursor.execute("UPDATE procurement SET status = 'Declined' WHERE id = ?", (row['id'],))
                conn.commit()
                st.rerun()
    else:
        st.info("No pending procurement requests.")

# --- 3. DATABASE CONTROL & RESET ---
with admin_tab3:
    st.subheader("Database Maintenance & System Reset")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    tables = [r[0] for r in cursor.fetchall()]

    selected_table = st.selectbox("Select Table to Clear", tables if tables else ["None"])
    confirm_clear = st.checkbox(f"Confirm wiping table '{selected_table}'")
    if st.button("Clear Selected Table", disabled=not confirm_clear):
        cursor.execute(f"DELETE FROM {selected_table}")
        conn.commit()
        st.success(f"Cleared table `{selected_table}`.")
        st.rerun()

conn.close() 