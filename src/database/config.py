import os
import streamlit as st
from supabase import create_client


def _get_secret(key: str) -> str | None:
    return st.secrets.get(key) if hasattr(st, 'secrets') else None or os.getenv(key)

SUPABASE_URL = _get_secret("SUPABASE_URL")
SUPABASE_KEY = _get_secret("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    st.error(
        "Supabase credentials are missing. Set SUPABASE_URL and SUPABASE_KEY in Streamlit Cloud secrets or environment variables."
    )
    st.stop()

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)