import streamlit as st
from TTS.api import TTS
import tempfile
import os
import sys

# Show Python path
st.write(f"🔧 Python used: `{sys.executable}`")

# Load and cache the TTS model
@st.cache_resource
def load_tts_model():
    return TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2").to("cpu")

tts = load_tts_model()

# App title
st.title("🎙️ Custom AI Voice Cloner")
st.markdown("Generate speech in a cloned voice using **XTTS-v2** and a fixed reference voice.")

# Step 1: Choose input method
input_mode = st.radio("Step 1️⃣: Choose input method", ("Enter text", "Upload file"))

text = ""
if input_mode == "Enter text":
    text = st.text_area("📝 Enter the text for the AI to speak:")
elif input_mode == "Upload file":
    uploaded_file = st.file_uploader("📄 Upload a `.txt`, `.csv`, or `.json` file", type=["txt", "csv", "json"])
    if uploaded_file:
        try:
            text = uploaded_file.read().decode("utf-8")
            st.success("✅ File loaded successfully.")
        except Exception as e:
            st.error(f"❌ Failed to read file: {e}")

# Step 2: Use static reference speaker audio
st.subheader("Step 2️⃣: 🔉 Reference Speaker Audio")
reference_wav_path = "data/processed/reference.wav"

if os.path.exists(reference_wav_path):
    st.audio(reference_wav_path, format="audio/wav")
    st.info("Using the default reference voice.")
else:
    st.error("❌ Reference voice not found. Make sure `data/processed/reference.wav` exists.")

# Step 3: Generate speech
st.subheader("Step 3️⃣: 🧠 Generate Cloned Speech")

if st.button("🔊 Generate Speech"):
    if not text.strip():
        st.warning("⚠️ Please enter or upload some text.")
    elif not os.path.exists(reference_wav_path):
        st.error("❌ Reference audio file not found.")
    else:
        with st.spinner("Synthesizing speech..."):
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_output:
                    output_path = tmp_output.name

                tts.tts_to_file(
                    text=text,
                    speaker_wav=reference_wav_path,
                    language="en",
                    file_path=output_path
                )

                st.success("✅ Speech generated successfully!")
                st.audio(output_path, format="audio/wav")
                with open(output_path, "rb") as audio_file:
                    st.download_button("⬇️ Download Cloned Voice", data=audio_file, file_name="cloned_voice.wav")

            except Exception as e:
                st.error(f"❌ Error during synthesis: {e}")
else:
    st.caption("Enter some text to begin.")
