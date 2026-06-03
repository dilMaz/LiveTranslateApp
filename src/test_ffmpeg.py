import os
import shutil

ffmpeg_path = r"C:\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin"

os.environ["PATH"] = ffmpeg_path + os.pathsep + os.environ["PATH"]

print("PATH ADDED:")
print(ffmpeg_path)

print("\nFFmpeg Found:")
print(shutil.which("ffmpeg"))