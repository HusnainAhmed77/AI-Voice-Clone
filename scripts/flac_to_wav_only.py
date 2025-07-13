import os
import librosa
import soundfile as sf
from tqdm import tqdm

# Input and output directories
input_dir = "data/raw"
output_dir = "data/processed"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Convert each .flac file to .wav
for file in tqdm(os.listdir(input_dir)):
    if file.endswith(".flac"):
        input_path = os.path.join(input_dir, file)
        output_path = os.path.join(output_dir, file.replace(".flac", ".wav"))

        # Load audio and resample to 22050 Hz
        y, sr = librosa.load(input_path, sr=22050)
        sf.write(output_path, y, sr)

print(f"✅ Converted all .flac files to .wav in: {output_dir}")
