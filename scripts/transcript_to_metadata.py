import os

input_path = "data/raw/transcript.txt"
output_path = "data/processed/metadata.csv"

# Ensure the processed folder exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(input_path, "r") as infile, open(output_path, "w") as outfile:
    for line in infile:
        parts = line.strip().split(" ", 1)
        if len(parts) == 2:
            utt_id, transcript = parts
            outfile.write(f"{utt_id}.wav|{transcript.strip()}\n")

print(f"✅ metadata.csv created at: {output_path}")
