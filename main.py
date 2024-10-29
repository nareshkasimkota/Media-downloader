from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import os
import sys
import yt_dlp

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; you can specify a list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods {GET, POST, etc.}
    allow_headers=["*"],  # Allows all headers
)

# Get the current directory
cur_dir = os.getcwd()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Media Downloader!"}

@app.get("/favicon.ico")
async def favicon():
    return {}  # You can serve a favicon here if you have one


@app.post("/download")
def download_video(link: str = Form(...)):
    youtube_dl_options = {
        "format": "best",  # Selects the best quality available
        "outtmpl": os.path.join(cur_dir, f"%(title)s.%(ext)s")  # Save with the video title and extension
    }
    
    # Use yt_dlp to download the video
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:  # Fixed: 'YoutubeDL' instead of 'YotubeDL'
        ydl.download([link])
    
    return {"status": "Download started", "message": f"Video from {link} is being downloaded"}
 