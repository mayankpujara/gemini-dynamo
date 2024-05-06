from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class VideoAnalysisRequest(BaseModel):
    youtube_link: HttpUrl
    # advanced settings

app = FastAPI()

@app.post("/analyse_video")

def analyse_video(request:VideoAnalysisRequest):

    loader = YoutubeLoader.from_youtube_url(str(request.youtube_link), add_video_info=True)
    docs = loader.load()

    print(f"On Loading: {type(docs)}")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap = 0)
    result = text_splitter.split_documents(docs)

    print(f"{type(docs)}")
    author = result[0].metadata['author']
    length = result[0].metadata['length']
    title = result[0].metadata['title']
    total_size = len(result)

    return {
        "author": author,
        "length": length,
        "title": title,
        "total_size": total_size,
    }

@app.get("/root")
def health():
    return {"status": "OK"}