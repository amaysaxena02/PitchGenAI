import streamlit as st
from generators.pitch_generator import generate_pitch
from utils.helpers import save_pitch

st.set_page_config(page_title="Startup Pitch AI", page_icon="🚀", layout="centered")
st.title("🚀 AI Startup Pitch Generator")

st.markdown("Enter your startup details below and generate a persuasive pitch for investors.")

with st.form("pitch_form"):
    name = st.text_input("Startup Name")
    problem = st.text_area("Problem", height=100)
    solution = st.text_area("Solution", height=100)
    market = st.text_input("Target Market")
    business_model = st.text_input("Business Model")
    tone = st.selectbox("Pitch Tone", ["formal", "persuasive", "storytelling"])
    submitted = st.form_submit_button("Generate Pitch")

if submitted:
    if not name or not problem or not solution:
        st.warning("Please fill in at least Name, Problem, and Solution fields.")
    else:
        startup_info = {
            "name": name,
            "problem": problem,
            "solution": solution,
            "market": market,
            "business_model": business_model,
            "tone": tone
        }
        with st.spinner("Generating pitch..."):
            pitch_text = generate_pitch(startup_info)

        st.subheader("📝 Generated Pitch Script")
        st.text_area("Pitch", value=pitch_text, height=300)

        file_path = save_pitch(pitch_text)
        st.success(f"Pitch saved to {file_path}")
        st.download_button("📥 Download Pitch", data=pitch_text, file_name=file_path.split('/')[-1])
