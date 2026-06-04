from deep_translator import GoogleTranslator
from gtts import gTTS
import os

def translate_to_sinhala(text):

    return GoogleTranslator(
        source="en",
        target="si"
    ).translate(text)


def generate_audio(text):

    os.makedirs("output", exist_ok=True)

    audio_path = "output/sinhala_audio.mp3"

    tts = gTTS(
        text=text,
        lang="si"
    )

    tts.save(audio_path)

    return audio_path


def generate_subtitle(text):

    os.makedirs("subtitles", exist_ok=True)

    subtitle_path = "subtitles/sinhala_subtitles.srt"

    srt_content = f"""1
00:00:00,000 --> 00:01:00,000
{text}
"""

    with open(
        subtitle_path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(srt_content)

    return subtitle_path