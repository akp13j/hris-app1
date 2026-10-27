import streamlit as st
import datetime

# Define dropdown option lists (1950 to current year)
YEARS = list(range(1950, datetime.date.today().year + 1))[::-1]
MONTHS = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]
DAYS = list(range(1, 32))

def render_staff_profile_form():
    st.title("📄 Staff Profile Form")
    st.caption("Please fill out all relevant details to complete your staff profile record.")

    with st.form("exact_staff_profile_form", clear_on_submit=False):
        
        # ---------------------------------------------------------
        # 1. PERSONAL INFORMATION
        # ---------------------------------------------------------
        st.header("1. Personal Details")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            name = st.text_input("Name")
            
            # --- DATE OF BIRTH DROPDOWNS (1950 - 2026) ---
            st.write("**Date of Birth**")
            dob_col1, dob_col2, dob_col3 = st.columns(3)
            with dob_col1:
                dob_year = st.selectbox("Year", YEARS, index=YEARS.index(1995), key="dob_yr")
            with dob_col2:
                dob_month = st.selectbox("Month", MONTHS, index=0, key="dob_mo")
            with dob_col3:
                dob_day = st.selectbox("Day", DAYS, index=0, key="dob_dy")
            
            dob_str = f"{dob_year}-{MONTHS.index(dob_month)+1:02d}-{dob_day:02d}"

            age = st.number_input("Age", min_value=0, max_value=120, value=25)
            father_name = st.text_input("Father's Name")
            
        with c2:
            mother_name = st.text_input("Mother's Name")
            nationality = st.text_input("Nationality")
            ethnicity = st.text_input("Ethnicity")
            religion = st.text_input("Religion")
            
        with c3:
            blood_type = st.selectbox("Blood Type", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "Unknown"])
            marital_status = st.selectbox("Marital Status", ["Single", "Married", "Other"])
            spouse_name = st.text_input("Spouse Name (If Married)")
            
            # --- STARTING WORK DATE DROPDOWNS ---
            st.write("**Starting Work Date**")
            st_col1, st_col2, st_col3 = st.columns(3)
            with st_col1:
                st_year = st.selectbox("Year", YEARS, index=0, key="st_yr")
            with st_col2:
                st_month = st.selectbox("Month", MONTHS, index=0, key="st_mo")
            with st_col3:
                st_day = st.selectbox("Day", DAYS, index=0, key="st_dy")

        st.divider()

        # ---------------------------------------------------------
        # 2. HEALTH STATUS & IDENTITY DOCUMENTS
        # ---------------------------------------------------------
        st.header("2. Health Status & Identification")
        
        col_health, col_id = st.columns(2)
        
        with col_health:
            st.subheader("Health Status")
            st.caption("Please describe if you have any other health problem")
            hearing = st.radio("Hearing", ["Good", "Not Good"], horizontal=True)
            seeing = st.radio("Seeing", ["Good", "Not Good"], horizontal=True)
            health_remark = st.text_area("Health Remarks / Other Problems", placeholder="Describe hearing, seeing or general health issues...")

        with col_id:
            st.subheader("Identity Card / Documents")
            st.caption("Select all valid identification cards you possess:")
            passport = st.checkbox("Passport")
            nrc = st.checkbox("NRC Card")
            mtc = st.checkbox("MTC Card")
            unhcr = st.checkbox("UNHCR Card")
            knu = st.checkbox("KNU Card")
            thai_residency = st.checkbox("Ten-Year Thai Residency Card")
            other_id_check = st.checkbox("Other ID")
            other_id_type = st.text_input("If Other ID, indicate type/number:")

        st.divider()

        # ---------------------------------------------------------
        # 3. ADDRESSES & CONTACTS
        # ---------------------------------------------------------
        st.header("3. Address & Contact Details")
        
        tab_pres, tab_pob, tab_parent = st.tabs([
            "🏡 Present Address", 
            "📍 Place of Birth / Previous Address", 
            "👪 Parent Address"
        ])

        with tab_pres:
            p1, p2, p3 = st.columns(3)
            p1.text_input("Village (Present)")
            p1.text_input("Section (Present)")
            p1.text_input("House No (Present)")
            
            p2.text_input("Road (Present)")
            p2.text_input("Township (Present)")
            p2.text_input("District (Present)")
            
            p3.text_input("Province (Present)")
            p3.text_input("Post Code (Present)")
            p3.text_input("Country (Present)")
            
            pc1, pc2, pc3 = st.columns(3)
            pc1.text_input("Phone (Present)")
            pc2.text_input("Email (Present)")
            pc3.text_input("Facebook / Messenger (Present)")

        with tab_pob:
            b1, b2, b3 = st.columns(3)
            b1.text_input("Village (Birth/Prev)")
            b1.text_input("Section (Birth/Prev)")
            b1.text_input("House No (Birth/Prev)")
            
            b2.text_input("Road (Birth/Prev)")
            b2.text_input("Township (Birth/Prev)")
            b2.text_input("District (Birth/Prev)")
            
            b3.text_input("Province (Birth/Prev)")
            b3.text_input("Post Code (Birth/Prev)")
            b3.text_input("Country (Birth/Prev)")
            
            bc1, bc2, bc3 = st.columns(3)
            bc1.text_input("Phone (Birth/Prev)")
            bc2.text_input("Email (Birth/Prev)")
            bc3.text_input("Facebook / Messenger (Birth/Prev)")

        with tab_parent:
            r1, r2, r3 = st.columns(3)
            r1.text_input("Village (Parent)")
            r1.text_input("Section (Parent)")
            r1.text_input("House No (Parent)")
            
            r2.text_input("Road (Parent)")
            r2.text_input("Township (Parent)")
            r2.text_input("District (Parent)")
            
            r3.text_input("Province (Parent)")
            r3.text_input("Post Code (Parent)")
            r3.text_input("Country (Parent)")
            
            rc1, rc2, rc3 = st.columns(3)
            rc1.text_input("Phone (Parent)")
            rc2.text_input("Email (Parent)")
            rc3.text_input("Facebook / Messenger (Parent)")

        st.divider()

        # ---------------------------------------------------------
        # 4. EMERGENCY CONTACT & DEPENDENTS
        # ---------------------------------------------------------
        st.header("4. Emergency Contact & Dependents")
        
        ec1, ec2 = st.columns(2)
        with ec1:
            st.subheader("Person to be notified in case of emergency")
            em_name = st.text_input("Emergency Contact Name")
            em_rel = st.text_input("Related to the applicant as")
            em_addr = st.text_input("Emergency Contact Address")
            em_phone = st.text_input("Emergency Contact Phone")
            em_email = st.text_input("Emergency Contact Email")
            em_fb = st.text_input("Emergency Contact Facebook/Messenger")

        with ec2:
            st.subheader("Dependents")
            num_deps = st.number_input("Number of dependents in you", min_value=0, value=0)
            st.caption("*(Child, wife, husband, Nephew, disabled person, Handicaps, Elder Person, who are dependent on you and without income)*")

        st.divider()

        # ---------------------------------------------------------
        # 5. EDUCATION
        # ---------------------------------------------------------
        st.header("5. Education")
        
        edu_levels = [
            "High school", "Post-Ten", "Diploma (College)", 
            "Bachelor (University)", "Master", "Doctor", "PHD"
        ]
        
        st.write("**Educational Attainment:**")
        for level in edu_levels:
            c_lvl, c_inst, c_maj, c_plc, c_prd, c_cert = st.columns([1.5, 2, 1.5, 1.5, 1.2, 1])
            chk = c_lvl.checkbox(level, key=f"edu_{level}")
            if chk:
                inst = c_inst.text_input(f"Institution ({level})", key=f"inst_{level}")
                maj = c_maj.text_input(f"Major ({level})", key=f"maj_{level}")
                plc = c_plc.text_input(f"Place ({level})", key=f"plc_{level}")
                prd = c_prd.text_input(f"Period ({level})", key=f"prd_{level}")
                cert = c_cert.selectbox(f"Cert/Dip", ["Yes", "No"], key=f"cert_{level}")

        st.divider()

        # ---------------------------------------------------------
        # 6. TRAININGS & WORKSHOPS
        # ---------------------------------------------------------
        st.header("6. Training, Workshop & Congress Attendance")
        
        tr_tab1, tr_tab2 = st.tabs(["🏥 Health Training", "💼 Management & Leadership Training"])
        
        with tr_tab1:
            health_trainings = [
                "Medical Doctor", "Master of Public Health", "Physician Assistant (PA)", "Health Assistant (HA)", 
                "Medic", "Emergency Obstetric Care (EmOC)", "Basic Emergency Obstetric Care (BeMOC)", 
                "Maternal Child Health (MCH)", "Nurse", "Nurse Aid", "Midwife", "Auxiliary Midwife", 
                "Community Health Worker (CHW)", "Public Health Institute (PHI)", "Laboratory", 
                "Health Facility Management", "Pharmacy Management", "Dental", "Trauma Management", 
                "Eye Care", "Mental Health", "Clinical Management Internship", "First Aid", 
                "Traditional Medicine", "Acupuncture", "Certificate of Public Health", 
                "Integrated Maternal Child Illnesses (IMCI)", "CHW TOT", "Health Facility Management TOT", 
                "Continuous Medical Education (CME) TOT", "Gender Base Violence"
            ]
            st.write("Select attended health trainings:")
            selected_health = st.multiselect("Health Trainings Attended", health_trainings)

        with tr_tab2:
            mgmt_trainings = [
                "Leadership", "Computer", "Health Information System (HIS)/ Data", "Finance Management", 
                "Accounting", "Proposal Writing", "Report Writing", "Project Cycle Management", 
                "Community Organizing", "Community Mobilization", "Advocacy", "Office Management", 
                "Human Resources Management", "Supply Chain/ Logistic and Procurement Management", 
                "Organization Development", "Mapping", "Fundraising", "Publication Training", 
                "Photo Documentation", "Video Documentation", "Disability Inclusion", "Social Security", 
                "Vehicle", "Feedback Mechanism", "Child Protection/ Child Right", "Human Right", 
                "Women Right", "Information Technology"
            ]
            st.write("Select attended management/leadership trainings:")
            selected_mgmt = st.multiselect("Management/Leadership Trainings Attended", mgmt_trainings)

        st.divider()

        # ---------------------------------------------------------
        # 7. WORK EXPERIENCE & CURRENT POSITION
        # ---------------------------------------------------------
        st.header("7. Work Experience & Current Position")
        
        st.subheader("Prior Work Experience & Volunteer")
        w1, w2, w3, w4, w5 = st.columns([2, 1.5, 2, 2.5, 1.5])
        w1.text_input("Organization / Clinic (Past)")
        w2.text_input("Period (From - To)")
        w3.text_input("Position (Past)")
        w4.text_input("Main Responsibility (Past)")
        w5.number_input("Salary/Stipend Amount (Past)", min_value=0.0)

        st.subheader("Organization Current Position")
        cp1, cp2, cp3, cp4 = st.columns(4)
        curr_org = cp1.text_input("Organization / Clinic")
        curr_pos = cp2.text_input("Position Title")
        curr_duty = cp4.text_input("Duty Station")
        
        cp5, cp6 = st.columns([3, 1])
        curr_resp = cp5.text_area("Main Responsibility")
        curr_sal = cp6.number_input("Salary / Stipend Amount", min_value=0.0)

        st.divider()

        # ---------------------------------------------------------
        # 8. CURRENT BENEFITS
        # ---------------------------------------------------------
        st.header("8. Current Benefits")
        
        benefit_types = [
            "Accommodation", "Food Ration", "Travel Fee", "Land", 
            "Leave", "Social Support", "Health Insurance", "Per-diem", "Honor Award"
        ]
        
        ben_cols1, ben_cols2 = st.columns(2)
        for idx, ben in enumerate(benefit_types):
            col = ben_cols1 if idx % 2 == 0 else ben_cols2
            with col:
                st.selectbox(f"Benefit: {ben}", ["No", "Yes"], key=f"ben_{ben}")

        st.divider()

        # ---------------------------------------------------------
        # 9. LANGUAGE, COMPUTER & OTHER SKILLS
        # ---------------------------------------------------------
        st.header("9. Skills & Languages")
        
        sk_col1, sk_col2, sk_col3 = st.columns(3)
        
        with sk_col1:
            st.subheader("Language Ability")
            for lang in ["Sgaw-Karen", "Poe-Karen", "English", "Burmese"]:
                st.write(f"**{lang}**")
                st.selectbox(f"Speaking ({lang})", ["Good", "Fair", "Poor"], key=f"spk_{lang}")
                st.selectbox(f"Writing ({lang})", ["Good", "Fair", "Poor"], key=f"wrt_{lang}")
                st.selectbox(f"Reading ({lang})", ["Good", "Fair", "Poor"], key=f"rd_{lang}")

        with sk_col2:
            st.subheader("Computer Skills")
            comp_skills = [
                "Microsoft Word", "Microsoft Excel", "Microsoft PowerPoint", 
                "Email", "Internet", "Basic Maintenance (install Window, Printer)", 
                "Photoshop", "Access Data base"
            ]
            for comp in comp_skills:
                st.selectbox(comp, ["Good", "Fair", "Poor"], key=f"comp_{comp}")

        with sk_col3:
            st.subheader("Other Skills")
            other_skills = [
                "Office Management", "Finance Management", "Human Resources Management", 
                "Proposal Writing", "Report Writing", "Public Speaking", 
                "Communication", "Facilitation", "Program Management", 
                "Supervising and Leading", "Advocate", "Critical"
            ]
            for oth in other_skills:
                st.selectbox(oth, ["Good", "Fair", "Poor"], key=f"oth_{oth}")

        st.divider()
        # ---------------------------------------------------------
        # 10. PERSONAL STATEMENT & QUESTIONS
        # ---------------------------------------------------------
        st.header("10. Personal Statement & Feedback")
        
        q1 = st.text_area("Why are you interested in HISWG/Training?", height=100)
        q2 = st.text_area("What is your hobby?", height=100)
        q3 = st.text_area("Please provide any further information about yourself which will allow our organization to know you better:", height=150)

        # MUST be inside render_staff_profile_form() and inside the st.form block:
        submitted = st.form_submit_button("💾 Save & Submit Staff Profile", type="primary")
        if submitted:
            profile_payload = {
                "name": name,
                "dob": dob_str,
                "age": age,
                "father_name": father_name,
                "mother_name": mother_name,
                "nationality": nationality,
                "ethnicity": ethnicity,
                "religion": religion,
                "blood_type": blood_type,
                "marital_status": marital_status,
                "spouse_name": spouse_name,
                "enrollment_date": f"{st_year}-{MONTHS.index(st_month)+1:02d}-{st_day:02d}",
                "hearing": hearing,
                "seeing": seeing,
                "health_remark": health_remark,
                "curr_org": curr_org,
                "curr_pos": curr_pos,
                "duty_station": curr_duty,
                "salary": curr_sal
            }
            save_staff_profile(profile_payload)
            st.success("✅ Staff Profile Form submitted and saved to database!")