from TTS.api import TTS

# Load the pre-trained XTTS-v2 model
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2").to("cpu")  # or "cuda"

# Path to the reference speaker audio (voice clone from LibriSpeech speaker 50561)
reference_wav = "data/processed/reference.wav"

# Ask the user for custom input text
text = input("🗣️ Enter the text you want the cloned voice to speak: ")

# Output file path
output_path = "output.wav"

# Generate speech in the cloned voice
tts.tts_to_file(
    text=text,
    speaker_wav=reference_wav,
    language="en",
    file_path=output_path
)

print(f"\n✅ Synthesized audio saved to: {output_path}")
