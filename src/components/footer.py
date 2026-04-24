import streamlit as st

def footer_home():
    name = "Parshuram"
    accent_color = "#FFFC00" 
    st.markdown(f"""
        <div style="margin-top: 3rem; display: flex; gap: 8px; justify-content: center; align-items: center;">
            <p style="font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: 1.1rem; color: white; margin: 0; letter-spacing: 0.5px;">
                Created with ❤️ by 
            </p>  
            <p style="font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 900; font-size: 1.1rem; color: {accent_color}; margin: 0; text-transform: uppercase;">
                {name}
            </p>
        </div>
    """, unsafe_allow_html=True)

def footer_dashboard():
    name = "Parshuram"
    accent_color = "#5865F2" 
    st.markdown(f"""
        <div style="margin-top: 3rem; display: flex; gap: 8px; justify-content: center; align-items: center;">
            <p style="font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: 1.1rem; color: #1A1C2E; margin: 0; letter-spacing: 0.5px;">
                Created with ❤️ by 
            </p>  
            <p style="font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 900; font-size: 1.1rem; color: {accent_color}; margin: 0; text-transform: uppercase;">
                {name}
            </p>
        </div>
    """, unsafe_allow_html=True)