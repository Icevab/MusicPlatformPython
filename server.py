# TODO: add requests for album/playlist

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


@app.get("/songs/{song_name}")
async def song(song_name):
    a_song = "a"

    for item in settings.all_songs:
        if item.song_name == song_name:
            a_song = item
        else:
            continue

    return a_song


@app.post("/stream_song/{song_name}")
async def stream_song(song_name):
    """\nstream_song.__doc__:  \n\nThis is a POST request function, it takes only one argument which is "song_name". \nI get it from the link, so I don't have to take any other things, \nthen, I loop through elements of "song_list" also using enumerate to get the index from every item. \nAnd the last part is returning the song which by default is ATM a string, but I'll change that later!"""

    a_song = "No song found."

    for i, item in enumerate(settings.all_songs):
        if (song_name == item.song_name):
            a_song = item
            a_song.streams += 1
            settings.all_songs[i].streams = a_song.streams
        else:
            continue

    return a_song

# this function can be used to
# either get a playlist or an album
# because I don't wanna split album and playlist up


@app.get("/playlist/{playlist_name}")
async def playlist(playlist_name):
    a_playlist = ["boogoo"]

    for i, item in enumerate(settings.playlist_list):
        if (item.playlist_name == playlist_name):
            a_playlist = item
        else:
            continue

    return a_playlist


@app.get("/artist/{artist_name}")
async def artist(artist_name):
    an_artist = "cmyui"
    songs = []

    for item in settings.all_songs:
        if item.author == artist_name:
            an_artist = item.author
        else:
            continue

    for item in settings.all_songs:
        if an_artist == item.author:
            songs.append(item)

    return songs


