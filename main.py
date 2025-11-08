from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI(title="OpenSoundWorld API", description="AI Music Generation & Visualization Demo", version="0.1")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head><title>OpenSoundWorld</title></head>
    <body style="font-family:Arial;text-align:center;margin-top:50px;">
        <h1>🎵 Welcome to OpenSoundWorld</h1>
        <p>This is an open-source AI music visualization project demo.</p>
        <p>Hosted on zmto.com Free VPS (non-commercial use)</p>
    </body>
    </html>
    """

@app.get("/generate_music")
def generate_music():
    """Simulated music generation API"""
    music_list = ["Lo-Fi Beat", "Ambient Piano", "Jazz Groove", "Blues Solo"]
    return {"status": "success", "generated": random.choice(music_list)}
