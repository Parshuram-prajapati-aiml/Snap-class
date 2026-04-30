import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home

# --- 1. DEFINE HELPERS FIRST ---

def _role_pill(label: str, kind: str) -> str:
    is_student = kind == "student"
    color  = "#C8FF00"               if is_student else "#648CFF"
    bg     = "rgba(200,255,0,0.08)"  if is_student else "rgba(100,140,255,0.08)"
    border = "rgba(200,255,0,0.25)"  if is_student else "rgba(100,140,255,0.25)"
    return f"""
    <div style="display:inline-flex; align-items:center; gap:6px; border-radius:100px; padding:5px 14px; background:{bg}; color:{color}; border:1px solid {border}; font-family:'DM Sans',sans-serif; font-size:11px; font-weight:600; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:.75rem;">
        <span style="width:6px;height:6px;border-radius:50%; background:{color};display:inline-block;"></span>
        {label}
    </div>"""

def _card_desc(text: str) -> str:
    return f"""<p style="font-family:'DM Sans',sans-serif; font-size:13px; color:rgba(255,255,255,0.4); line-height:1.6; margin:.25rem 0 1.25rem;">{text}</p>"""


# --- 2. DEFINE MAIN FUNCTION SECOND ---

def home_screen():
    style_background_home()
    style_base_layout()

    header_home()

    st.markdown("""
        <div style="text-align:center; margin-top: -15px; margin-bottom: 2.5rem;">
            <h1 style="
                font-family:'Bebas Neue',sans-serif;
                font-size:clamp(2.5rem, 10vw, 4.5rem); line-height:0.9;
                letter-spacing:clamp(1px, 1vw, 4px); color:#FFFFFF;
                margin:0; word-break:break-word;
            ">
                SNAP<br>
                <span style="color:#C8FF00; padding-left:clamp(8px, 3vw, 30px);">CLASS</span>
            </h1>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        # Now Python knows what _role_pill is!
        st.markdown(_role_pill("Student", "student"), unsafe_allow_html=True)
        st.markdown("<h2 style='color:white; margin:0;'>I'm Student</h2>", unsafe_allow_html=True)
        st.markdown(_card_desc("Access classes, assignments, and your progress."), unsafe_allow_html=True)
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=180)
        if st.button("Student Portal  →", key="student_btn", use_container_width=True):
            st.session_state["login_type"] = "student"
            st.rerun()

    with col2:
        st.markdown(_role_pill("Teacher", "teacher"), unsafe_allow_html=True)
        st.markdown("<h2 style='color:white; margin:0;'>I'm Teacher</h2>", unsafe_allow_html=True)
        st.markdown(_card_desc("Manage classes, track performance, and create content."), unsafe_allow_html=True)
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=220)
        if st.button("Teacher Portal  →", key="teacher_btn", use_container_width=True):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    footer_home()