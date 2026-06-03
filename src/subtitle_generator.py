import os
import whisper
from deep_translator import GoogleTranslator

# FFmpeg path
ffmpeg_path = r"C:\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin"
os.environ["PATH"] = ffmpeg_path + os.pathsep + os.environ["PATH"]

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)

    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

print("Loading model...")
model = whisper.load_model("base")

print("Processing video...")
result = model.transcribe("videos/test_video.mp4")

srt_content = ""

for i, segment in enumerate(result["segments"], start=1):

    translated_text = GoogleTranslator(
        source="en",
        target="si"
    ).translate(segment["text"])

    start_time = format_time(segment["start"])
    end_time = format_time(segment["end"])

    srt_content += f"{i}\n"
    srt_content += f"{start_time} --> {end_time}\n"
    srt_content += f"{translated_text}\n\n"

with open(
    "subtitles/sinhala_subtitles.srt",
    "w",
    encoding="utf-8"
) as file:
    file.write(srt_content)

print("Real subtitle file created successfully!")