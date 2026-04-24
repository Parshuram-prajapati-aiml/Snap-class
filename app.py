
import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    st.set_page_config(
        page_title='SnapClass - Making Attendance faster using AI',
        page_icon= "https://i.ibb.co/YTYGn5qV/logo.png"
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()
        
        case None:
            home_screen()


    join_code = st.session_state.get('pending_join_code')
    if join_code is None:
        join_code_value = st.query_params.get('join-code')
        if isinstance(join_code_value, list) and join_code_value:
            join_code = join_code_value[0]
        elif isinstance(join_code_value, str):
            join_code = join_code_value

        if join_code:
            st.session_state['pending_join_code'] = str(join_code).strip()
            remaining_params = {k: v for k, v in st.query_params.items() if k != 'join-code'}
            st.experimental_set_query_params(**remaining_params)

    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()

main()