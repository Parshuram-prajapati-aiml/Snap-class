import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:white; border-left: 8px solid #EB459E; padding: clamp(12px, 4vw, 25px); border-radius: 20px; border: 1px solid black; margin-bottom:20px; box-sizing:border-box; width:100%; overflow:hidden;">
        <h3 style="margin:0; color: #1e293b; font-size: clamp(1rem, 4vw, 1.5rem); word-break:break-word; overflow-wrap:break-word;">{name}</h3>
        <p style="color:#64748b; margin:10px 0; font-size: clamp(0.78rem, 3vw, 0.9rem); word-break:break-word; overflow-wrap:break-word;">Code : <span style="background:#E0E3FF; color:#5865F2; padding:2px 8px; border-radius:5px; white-space:nowrap;">{code}</span> | Section : {section}</p>
        
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: #EB459E10; padding:5px 12px; border-radius:12px; font-size:0.9rem">{icon} <b>{value}</b> {label} </div>'
        
        html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
