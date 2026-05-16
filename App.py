--- CHUNK 1 ---
import streamlit as st
from datetime import date, datetime

st.set_page_config(page_title="Holiday Hunt", page_icon="🏖️", layout="wide", initial_sidebar_state="collapsed")

if "package_alerts" not in st.session_state:
    st.session_state.package_alerts = []
if "flight_alerts" not in st.session_state:
    st.session_state.flight_alerts = []
if "package_results" not in st.session_state:
    st.session_state.package_results = []
if "flight_results" not in st.session_state:
    st.session_state.flight_results = []
if "package_matches" not in st.session_state:
    st.session_state.package_matches = []

st.markdown(
    """
    <style>
    :root {
      --bg: #07152a;
      --panel: #0d2240;
      --panel-2: #123058;
      --text: #ffffff;
      --muted: #c9d7ef;
      --accent: #78a9ff;
      --accent-2: #3f7af7;
      --border: rgba(255,255,255,0.12);
    }
    .stApp {
      background: radial-gradient(circle at top left, #0c2142 0%, #07152a 55%, #05101f 100%);
      color: var(--text);
    }
    html, body, [class*="css"]  { color: var(--text); }
    .block-container { padding-top: 1.2rem; padding-bottom: 2rem; max-width: 1200px; }
    h1, h2, h3, h4, p, label, div, span { color: var(--text) !important; }
    .hero {
      background: linear-gradient(180deg, rgba(18,48,88,.95), rgba(13,34,64,.9));
      border: 1px solid var(--border); border-radius: 24px; padding: 1.2rem; margin-bottom: 1rem;
      box-shadow: 0 10px 30px rgba(0,0,0,.18);
    }
    .hero p { color: var(--muted) !important; margin-bottom: 0; }
    .panel {
      background: linear-gradient(180deg, rgba(18,48,88,.92), rgba(13,34,64,.88));
      border: 1px solid var(--border); border-radius: 22px; padding: 1rem; box-shadow: 0 8px 24px rgba(0,0,0,.16);
    }
    .metric-card {
      background: rgba(255,255,255,0.05); border: 1px solid var(--border); border-radius: 18px; padding: .9rem 1rem; margin-bottom: .6rem;
    }
    .small-muted { color: var(--muted) !important; font-size: 0.92re
