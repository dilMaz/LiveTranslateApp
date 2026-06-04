from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from deep_translator import GoogleTranslator
import os
from src.video_processor import generate_transcript

# Create FastAPI App
app = FastAPI(
    title="Live Translate App API",
    version="1.0"
)

# Request Model
class TranslationRequest(BaseModel):
    text: str


# Home Endpoint
@app.get("/")
def home():
    return {
        "project": "Live Translate App",
        "status": "Running",
        "version": "1.0"
    }


# Health Check
@app.get("/health")
def health():
    return {
        "message": "Backend Working Successfully"
    }


# Text Translation Endpoint
@app.post("/translate-text")
def translate_text(request: TranslationRequest):

    translated_text = GoogleTranslator(
        source="en",
        target="si"
    ).translate(request.text)

    return {
        "original_text": request.text,
        "translated_text": translated_text
    }


# Video Upload Endpoint
@app.post("/upload-video")
async def upload_video(file: UploadFile = File(...)):

    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "message": "Video uploaded successfully",
        "filename": file.filename,
        "saved_path": file_path
    }
@app.post("/translate-video")
async def translate_video(file: UploadFile = File(...)):

    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    transcript = generate_transcript(file_path)

    return {
        "filename": file.filename,
        "transcript": transcript
    }