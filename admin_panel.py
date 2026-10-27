import streamlit as st
import pandas as pd
from db import get_all_profiles, update_staff_profile, delete_staff_profile

def render_admin_panel():
    st.title("🛡️ Staff Management & Admin Panel")
    
    df = get_all_profiles()
    
    if df.empty:
        st.info("No staff profiles found in database. Submit profiles from the form first.")
        return

    # ---------------------------------------------------------
    # 1. SEARCH & EXPORT SECTION
    # ---------------------------------------------------------
    st.subheader("1. View & Export Records")
    
    col_s, col_exp1, col_exp2 = st.columns([3, 1, 1])
    search_term = col_s.text_input("🔍 Search Staff by Name or Position", "")
    
    filtered_df = df.copy()
    if search_term:
        filtered_df = filtered_df[
            filtered_df['name'].str.contains(search_term, case=False, na=False) | 
            filtered_df['curr_pos'].str.contains(search_term, case=False, na=False)
        ]

    st.dataframe(filtered_df, use_container_width=True)

    # Export to CSV Button
    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    col_exp1.download_button(
        label="📥 Export to CSV",
        data=csv_data,
        file_name="staff_profiles.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.divider()

    # ---------------------------------------------------------
    # 2. EDIT & DELETE SECTION
    # ---------------------------------------------------------
    st.subheader("2. Edit or Delete Staff Profile")
    
    # Select staff member to action
    staff_options = {f"ID {row['id']} - {row['name']} ({row['curr_pos']})": row['id'] for _, row in filtered_df.iterrows()}
    
    if not staff_options:
        st.warning("No records match your search.")
        return

    selected_label = st.selectbox("Select Staff Member to Modify:", list(staff_options.keys()))
    selected_id = staff_options[selected_label]
    selected_row = df[df['id'] == selected_id].iloc[0]

    tab_edit, tab_delete = st.tabs(["✏️ Edit Profile", "🗑️ Delete Profile"])

    # EDIT TAB
    with tab_edit:
        with st.form("edit_staff_form"):
            e1, e2 = st.columns(2)
            name = e1.text_input("Name", value=str(selected_row['name']))
            dob = e2.text_input("Date of Birth (YYYY-MM-DD)", value=str(selected_row['dob']))
            
            e3, e4 = st.columns(2)
            curr_pos = e3.text_input("Current Position", value=str(selected_row['curr_pos']))
            salary = e4.number_input("Salary", value=float(selected_row['salary'] or 0.0))
            
            duty_station = st.text_input("Duty Station", value=str(selected_row['duty_station']))
            
            submit_edit = st.form_submit_button("💾 Save Changes", type="primary")
            if submit_edit:
                updated_data = {
                    "name": name,
                    "dob": dob,
                    "age": selected_row['age'],
                    "father_name": selected_row['father_name'],
                    "mother_name": selected_row['mother_name'],
                    "nationality": selected_row['nationality'],
                    "ethnicity": selected_row['ethnicity'],
                    "religion": selected_row['religion'],
                    "blood_type": selected_row['blood_type'],
                    "marital_status": selected_row['marital_status'],
                    "spouse_name": selected_row['spouse_name'],
                    "enrollment_date": selected_row['enrollment_date'],
                    "hearing": selected_row['hearing'],
                    "seeing": selected_row['seeing'],
                    "health_remark": selected_row['health_remark'],
                    "curr_org": selected_row['curr_org'],
                    "curr_pos": curr_pos,
                    "duty_station": duty_station,
                    "salary": salary
                }
                update_staff_profile(selected_id, updated_data)
                st.success("✅ Staff profile updated successfully!")
                st.rerun()

    # DELETE TAB
    with tab_delete:
        st.warning(f"⚠️ Are you sure you want to permanently delete record for **{selected_row['name']}**?")
        if st.button("🔴 Confirm Delete", type="primary"):
            delete_staff_profile(selected_id)
            st.success("✅ Profile deleted.")
            st.rerun()