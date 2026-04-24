import streamlit as st
from PIL import Image
import numpy as np
import time

# UI & Style Imports
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card

# Logic & Data Imports
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance, unenroll_student_to_subject

def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']

    # --- TOP NAVIGATION BAR ---
    with st.container():
        c1, c2 = st.columns([2, 1], vertical_alignment='center')
        with c1:
            header_dashboard()
        with c2:
            st.markdown(f"<h3 style='margin:0; color:#5865F2;'>Hi, {student_data['name']} 👋</h3>", unsafe_allow_html=True)
            if st.button("Logout", key='logout_btn', help="Ctrl + Backspace"):
                st.session_state['is_logged_in'] = False
                if "student_data" in st.session_state:
                    del st.session_state.student_data 
                st.rerun()

    st.markdown("<hr style='margin: 1.5rem 0; opacity: 0.1;'>", unsafe_allow_html=True)

    # --- SUBJECTS HEADER ---
    c1, c2 = st.columns([2, 1], vertical_alignment='center')
    with c1:
        st.markdown("<h2 style='text-align: left; margin:0;'>Your Courses</h2>", unsafe_allow_html=True)
    with c2:
        if st.button('➕ Enroll New Subject', use_container_width=True):
            enroll_dialog()

    # --- DATA LOADING ---
    with st.spinner('Syncing your academic records...'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    # Attendance Logic
    stats_map = {}
    for log in logs:
        sid = log['subject_id']
        if sid not in stats_map: stats_map[sid] = {"total": 0, "attended": 0}
        stats_map[sid]['total'] += 1
        if log.get('is_present'): stats_map[sid]['attended'] += 1

    # --- SUBJECT GRID ---
    if not subjects:
        st.info("You haven't enrolled in any subjects yet. Click 'Enroll New Subject' to start!")
    else:
        cols = st.columns(2, gap="medium")
        for i, sub_node in enumerate(subjects):
            sub = sub_node['subjects']
            sid = sub['subject_id']
            stats = stats_map.get(sid, {"total": 0, "attended": 0})

            with cols[i % 2]:
                # We wrap the card to add a little hover lift via container
                with st.container(border=True):
                    subject_card(
                        name=sub['name'],
                        code=sub['subject_code'],
                        section=sub['section'],
                        stats=[
                            ('📅', 'Total Sessions', stats['total']),
                            ('✅', 'Attended', stats['attended']),
                        ]
                    )
                    # Inline unenroll action
                    if st.button(f"Unenroll {sub['subject_code']}", key=f"un_{sid}", type="secondary"):
                        unenroll_student_to_subject(student_id, sid)
                        st.toast(f"Removed {sub['name']}")
                        st.rerun()

    footer_dashboard()

def student_screen():
    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return
    
    # --- LOGIN SCREEN ---
    c1, c2 = st.columns([2, 1], vertical_alignment='center')
    with c1:
        header_dashboard()
    with c2:
        if st.button("← Back to Home", key='back_home'):
            st.session_state['login_type'] = None
            st.rerun()

    st.markdown("<h2 style='text-align: center;'>FaceID Login</h2>", unsafe_allow_html=True)
    
    # Modern Camera Container
    with st.container(border=True):
        photo_source = st.camera_input("Position your face clearly in the frame")

    if photo_source:
        img = np.array(Image.open(photo_source))
        with st.spinner('Verifying Identity...'):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.error('No face detected. Please try again.')
            elif num_faces > 1:
                st.warning('Multiple people detected. Only one person can login at a time.')
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id'] == student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.success(f"Access Granted: {student['name']}")
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info("Face not recognized. Let's create your account!")
                    
                    # --- REGISTRATION BOX ---
                    with st.container(border=True):
                        st.markdown("<h3>New Student Registration</h3>", unsafe_allow_html=True)
                        new_name = st.text_input("Full Name", placeholder='Enter your legal name')

                        st.markdown("<h4>Voice Enrollment (Optional)</h4>", unsafe_allow_html=True)
                        audio_data = st.audio_input('Record: "I am present for Snap Class"')

                        if st.button('✨ Create My Profile', type='primary', use_container_width=True):
                            if new_name:
                                with st.spinner('Encrypting biometrics...'):
                                    img = np.array(Image.open(photo_source))
                                    encodings = get_face_embeddings(img)
                                    if encodings:
                                        face_emb = encodings[0].tolist()
                                        voice_emb = get_voice_embedding(audio_data.read()) if audio_data else None

                                        response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)
                                        if response_data:
                                            train_classifier()
                                            st.session_state.student_data = response_data[0]
                                            st.success("Account Created Successfully!")
                                            time.sleep(1)
                                            st.rerun()
                                    else:
                                        st.error('Facial scan failed. Please adjust lighting.')
                            else:
                                st.warning('Name is required.')
        
    footer_dashboard()