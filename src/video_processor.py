import os
import whisper

# FFmpeg path
ffmpeg_path = r"C:\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin"
os.environ["PATH"] = ffmpeg_path + os.pathsep + os.environ["PATH"]

model = whisper.load_model("base")

def generate_transcript(video_path):

    result = model.transcribe(video_path)

    return result["text"]