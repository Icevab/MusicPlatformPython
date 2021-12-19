from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import settings

from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name: str
    length: int  # in seconds
    streams: int
    artists: list
    link: str


@app.get("/")
async def main():
    return {"song": f"{settings.song.song_name}"}


@app.get("/{song_name}")
async def song(song_name):
    return {"song_name": f"{settings.song.song_name}",
            "song_length": f"{settings.song.convert_length()}"}


@app.post("/song_stream/{song_name}")
async def stream_song(song_name):
    song = ""

    for i, item in enumerate(settings.song_list):
        if (song_name == item.song_name):
            song = item
            song.streams += 1
            settings.song_list[i].streams = song.streams
        else:
            continue

    return song
