import os

# FFmpeg Path
ffmpeg_path = r"C:\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin"
os.environ["PATH"] = ffmpeg_path + os.pathsep + os.environ["PATH"]

import whisper

video_path = "videos/test_video.mp4"

print("Loading model...")
model = whisper.load_model("base")

print("Starting transcription...")

result = model.transcribe(video_path)

print("\nFull Transcript:\n")
print(result["text"])

# Save transcript
with open(
    "transcripts/output.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(result["text"])

print("\nTranscript saved successfully!")

print("\n========== SEGMENTS ==========\n")

for segment in result["segments"]:
    print(segment)
    print()