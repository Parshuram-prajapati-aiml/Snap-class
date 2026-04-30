import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:0px; margin-top:30px">
            <img src='{logo_url}' style='height:100px;' />
        </div> 
        """, unsafe_allow_html=True)

def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:clamp(4px,2vw,10px); flex-wrap:wrap;">
            <img src='{logo_url}' style='height:clamp(50px, 10vw, 85px); width:auto;' />
            <h2 style='text-align:left; color:#FFFC00; font-size:clamp(1rem, 4vw, 1.5rem); margin:0; line-height:1.2;'>SNAP<br/>CLASS</h2>
        </div> 
        """, unsafe_allow_html=True)