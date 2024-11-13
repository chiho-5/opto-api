# intermediary.py
from fastapi import FastAPI, File, UploadFile
import requests
import shutil


app = FastAPI()

@app.post("/process-video")
async def process_video(file: UploadFile = File(...)):
    files = {"file": (file.filename, await file.read(), file.content_type)}
    response = requests.post("https://mvcloud--opto-ai-flask-app.modal.run/predict", files=files)
    return response.json()
