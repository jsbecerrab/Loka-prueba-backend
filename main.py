from typing import Optional
from fastapi import FastAPI, Depends
import base64
import requests as req


from utils.config import get_settings, Settings
from utils.consts import spotify_auth, spotify_url, spotify_search

app = FastAPI()

settings: Settings = get_settings()

token = base64.b64encode(str.encode(settings.client_id + ":" + settings.client_secret)).decode('utf-8')

headers = {'Content-Type': 'application/x-www-form-urlencoded', 
'Authorization': 'Basic ' + token}
data = {'grant_type': "client_credentials"}
url = spotify_auth
spotifyToken = req.post(url, data=data, headers=headers).json()

@app.get("/ping")
def read_root():
  return "Everything is ok :)"


@app.get("/search")
def search_spotify(q: str, type: str):
  headers = {'Authorization': 'Bearer ' + spotifyToken['access_token']}
  payload = {'q':q , 'type': type}
  response = req.get(spotify_url + spotify_search, headers=headers, params=payload)
  return response.json()