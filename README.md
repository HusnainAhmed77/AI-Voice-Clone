🎙️ Custom AI Voice Cloner using XTTS-v2

This project is a Streamlit-based app that allows you to clone a speaker's voice from a reference .wav file and generate speech from any input text using the 🗣️ XTTS-v2 model.

🚀 Features

✅ Upload a text prompt or text file (.txt, .csv, .json)
✅ Use a custom speaker .wav file to clone their voice
✅ Synthesize and playback generated speech in your browser
✅ Download the generated .wav output
✅ XTTS-v2 multilingual and multi-speaker support
✅ Fully local – no internet needed after setup
🖥️ Demo UI


1. Clone the Repository
git clone https://github.com/yourusername/voice-ai-clone.git
cd voice-ai-clone
2. (Recommended) Create Virtual Environment
python3 -m venv tts-env
source tts-env/bin/activate  # macOS/Linux
# tts-env\Scripts\activate.bat  # Windows
3. Install Dependencies
pip install -r requirements.txt
Make sure you have FFmpeg installed:

brew install ffmpeg  # macOS
sudo apt install ffmpeg  # Linux
▶️ Run the App

streamlit run app.py
Open in browser: http://localhost:8501

🛠️ How It Works

Choose Input Mode
"Enter text": Type text directly.
"Upload file": Upload .txt, .csv, or .json with speech content.
Upload Reference Audio
Upload a .wav file of the voice you want to clone.
This replaces the default reference.wav temporarily for inference.
Generate Speech
Click "Generate Speech"
Synthesized .wav audio will be played and available for download.
⚙️ Requirements

Python 3.8–3.10 recommended
torch, torchaudio, TTS, streamlit, scipy, numpy<2
You can downgrade numpy if you face compatibility issues:

pip install numpy==1.26.4
📦 Dependencies

Example requirements.txt:

streamlit==1.35.0
TTS==0.22.0
torch==2.1.2
torchaudio==2.1.2
scipy==1.13.1
numpy==1.26.4
💡 Notes

The app only performs inference – not model fine-tuning.
For best results, use clean .wav files around 10–30 seconds long.
Make sure your audio is 16-bit, mono-channel, 16kHz–22kHz format.
📌 TODO / Future Improvements

 Fine-tune the model on uploaded reference audio (optional)
 Add speaker voice history
 Deploy online with GPU acceleration
