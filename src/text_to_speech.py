from gtts import gTTS

with open(
    "translations/sinhala_output.txt",
    "r",
    encoding="utf-8"
) as file:
    sinhala_text = file.read()

tts = gTTS(
    text=sinhala_text,
    lang="si"
)

tts.save("output/sinhala_audio.mp3")

print("Sinhala audio generated!")