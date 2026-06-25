import streamlit as st
import subprocess
import threading
import time

# ---------------------------
# Custom CSS Styling
# ---------------------------
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #1f1c2c, #928dab);
            color: white;
        }
        h1 {
            text-align: center;
            color: #ffffff;
            font-size: 3rem !important;
            font-weight: 700;
            margin-bottom: 20px;
        }
        .card {
            background: rgba(255, 255, 255, 0.15);
            padding: 20px;
            border-radius: 12px;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            margin-bottom: 20px;
            border: 1px solid rgba(255,255,255,0.2);
        }
        iframe {
            border-radius: 12px;
            border: 2px solid rgba(255,255,255,0.3);
        }
        p, label, span {
            font-size: 1.1rem !important;
            color: #f0f0f0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# Start Flask server
# ---------------------------
def run_flask():
    subprocess.Popen(["python", "app.py"])

threading.Thread(target=run_flask).start()
time.sleep(2)

# ---------------------------
# Streamlit UI
# ---------------------------
st.title("Flask App Running on Streamlit Cloud")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.write("Below is your Flask app:")
st.markdown('</div>', unsafe_allow_html=True)

st.components.v1.iframe("http://localhost:5000", height=300)
