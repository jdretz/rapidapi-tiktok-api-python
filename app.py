import os
import json
import requests
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

app = Flask(__name__)

@app.route('/')
def hello_world():
    url = "https://tiktok.p.rapidapi.com/live/hashtag/feed"

    hashtag = "python"

    querystring = {"name": hashtag,"limit":"10"}
    headers = {
        'x-rapidapi-host': "tiktok.p.rapidapi.com",
        'x-rapidapi-key': RAPIDAPI_KEY
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=querystring
    )

    res_json = json.loads(response.text)
    videos = res_json['media']
    return render_template('tiktok.html', response=videos, hashtag=hashtag)

