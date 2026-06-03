from deep_translator import GoogleTranslator

# Read transcript
with open(
    "transcripts/output.txt",
    "r",
    encoding="utf-8"
) as file:
    english_text = file.read()

print("English Text:")
print(english_text)

print("\nTranslating...")

translated_text = GoogleTranslator(
    source="en",
    target="si"
).translate(english_text)

print("\nSinhala Translation:")
print(translated_text)

# Save translation
with open(
    "translations/sinhala_output.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(translated_text)

print("\nTranslation saved successfully!")