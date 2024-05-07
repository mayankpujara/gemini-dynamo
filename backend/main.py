from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from fastapi.middleware.cors import CORSMiddleware

from services.genai import YoutubeProcessor

class VideoAnalysisRequest(BaseModel):
    youtube_link: HttpUrl
    # advanced settings

app = FastAPI()

# Configure CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials =True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.post("/analyse_video")
def analyse_video(request:VideoAnalysisRequest):

    processor = YoutubeProcessor()
    result = processor.retrive_youtube_documents(str(request.youtube_link), verbose=True)


    return {
        "result": result
    }

@app.get("/root")
def health():
    return {"status": "OK"}