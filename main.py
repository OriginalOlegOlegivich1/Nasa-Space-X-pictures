import pathlib
from pathlib import Path
import requests
import os
from dotenv import load_dotenv
load_dotenv()
import pprint
from pprint import pprint


NASA_token = os.getenv("TOKEN")

url="https://api.nasa.gov/planetary/apod"

params = {
    "api_key": NASA_token,
    "count": 10
}

response = requests.get(url, params=params)
response.raise_for_status()
for i in range(10):
    picture_url = response.json() [i] ["url"] 

    picture_response = requests.get(picture_url, params=params)
    picture_response.raise_for_status()


    with open(f'наса/picture{i}.jpeg', "wb") as file:
        file.write(picture_response.content)
    print(picture_url)