import streamlit as st
from PIL import Image
import numpy as np
import time
from audio_recorder_streamlit import audio_recorder

# UI & Style Imports
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card

# Logic & Data Imports
# NOTE: face_pipeline & voice_pipeline are imported lazily inside functions
# to avoid loading dlib/cv2/torch on every render (makes login instant)
from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance, unenroll_student_to_subject
from src.components.dialog_auto_enroll import auto_enroll_dialog

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
    pending_join_code = st.session_state.get('pending_join_code')
    if pending_join_code:
        st.info(f"Join request detected for subject code **{pending_join_code}**. After login, click below to enroll.")
        if st.button('Join this class', use_container_width=True, key='join_with_code'):
            auto_enroll_dialog(pending_join_code)
            st.session_state.pop('pending_join_code', None)
            st.rerun()
        st.markdown("<hr style='margin: 1rem 0; opacity: 0.1;'>", unsafe_allow_html=True)

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

    pending_join_code = st.session_state.get('pending_join_code')
    if pending_join_code:
        st.info(f"Detected a join request for subject code **{pending_join_code}**. Please log in or register to complete enrollment.")
    
    # Modern Camera Container
    with st.container(border=True):
        photo_source = st.camera_input("Position your face clearly in the frame")

    if photo_source:
        img = np.array(Image.open(photo_source).convert('RGB'))
        with st.spinner('Verifying Identity...'):
            # Lazy import: load face pipeline only when a photo is taken
            from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
            from src.pipelines.voice_pipeline import get_voice_embedding
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.error('No face detected. Please try again.')
            elif num_faces > 1:
                st.warning('Multiple people detected. Only one person can login at a time.')
            else:
                matched_student = None
                if detected:
                    detected_id = int(list(detected.keys())[0])
                    all_students = get_all_students()
                    matched_student = next(
                        (s for s in all_students if int(s['student_id']) == detected_id),
                        None
                    )

                if matched_student:
                    st.session_state.is_logged_in = True
                    st.session_state.user_role = 'student'
                    st.session_state.student_data = matched_student
                    st.success(f"Access Granted: {matched_student['name']}")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.info("Face not recognized. Let's create your account!")

                    # --- REGISTRATION BOX ---
                    with st.container(border=True):
                        st.markdown("<h3>New Student Registration</h3>", unsafe_allow_html=True)
                        new_name = st.text_input("Full Name", placeholder='Enter your legal name')

                        st.markdown("<h4>🎙️ Voice Enrollment (Optional)</h4>", unsafe_allow_html=True)
                        st.caption("Press the mic button, speak clearly for 3–5 seconds, then press it again to stop.")
                        audio_data = audio_recorder(
                            text="",
                            recording_color="#e74c3c",
                            neutral_color="#5865F2",
                            icon_size="2x",
                            pause_threshold=3.0,
                            key="voice_enroll_recorder"
                        )
                        if audio_data:
                            st.audio(audio_data, format="audio/wav")
                            st.success("✅ Voice recorded! Submit below to save.")

                        if st.button('✨ Create My Profile', type='primary', use_container_width=True):
                            if not new_name or not new_name.strip():
                                st.warning('Name is required.')
                            else:
                                with st.spinner('Encrypting biometrics...'):
                                    encodings = get_face_embeddings(img)
                                    if not encodings:
                                        st.error('Facial scan failed. Please adjust lighting.')
                                    elif len(encodings) > 1:
                                        st.warning('Please use a single face for registration.')
                                    else:
                                        face_emb = encodings[0].tolist()
                                        voice_emb = get_voice_embedding(audio_data) if audio_data else None

                                        response_data = create_student(
                                            new_name,
                                            face_embedding=face_emb,
                                            voice_embedding=voice_emb,
                                        )
                                        if response_data:
                                            created_student = response_data[0]
                                            train_classifier()
                                            st.session_state.is_logged_in = True
                                            st.session_state.user_role = 'student'
                                            st.session_state.student_data = created_student
                                            st.success("Account Created Successfully!")
                                            time.sleep(1)
                                            st.rerun()
                                        else:
                                            st.error('Unable to create student profile. Please try again.')

    footer_dashboard()