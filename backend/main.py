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

genai_processor = GeminiProcessor(
    model_name= "gemini-pro",
    project = "radicalx-gemini-dynamo"
)


@app.post("/analyse_video")
def analyse_video(request:VideoAnalysisRequest):
    


    processor = YoutubeProcessor(genai_processor=genai_processor)
    result = processor.retrive_youtube_documents(str(request.youtube_link), verbose=True)

    #summary = genai_processor.generate_document_summary(result, verbose = True)

    # Find key concepts

    key_concepts = processor.find_key_concepts(result, verbose = True)
    
    return {
        "key_concepts": key_concepts
    }

@app.get("/root")
def health():
    return {"status": "OK"}