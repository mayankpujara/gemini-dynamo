from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from fastapi.middleware.cors import CORSMiddleware

from services.genai import (YoutubeProcessor, GeminiProcessor)

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

    genai_processor = GeminiProcessor(
        model_name= "gemini-pro",
        project = "radicalx-gemini-dynamo"
    )

    summary = genai_processor.generate_document_summary(result, verbose = True)

    return {
        "summary": summary
    }

@app.get("/root")
def health():
    return {"status": "OK"}