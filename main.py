# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import googleapiclient.discovery
import googleapiclient.errors
from dotenv import load_dotenv
import json

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
PLAYLIST_ID = 'PLfoNZDHitwjUv0pjTwlV1vzaE0r7UDVDR'

if not API_KEY:
    raise ValueError("A chave da API não foi encontrada. Verifique o arquivo .env.")

def main():

    api_service_name = "youtube"
    api_version = "v3"
    
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY)


    playlist_request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=PLAYLIST_ID,
        maxResults=25
    )
    playlist_response = playlist_request.execute()

    video_ids = [item["contentDetails"]["videoId"] for item in playlist_response["items"]]

    videos_request = youtube.videos().list(
        part="statistics, snippet, contentDetails",
        id=",".join(video_ids),
        maxResults=25
    )

    videos_response = videos_request.execute()

    # Filtrando os dados desejados
    filtered_data = [
        {
            "videoId": item["id"],
            "publishedAt": item["snippet"]["publishedAt"],
            "title": item["snippet"]["title"],
            "viewCount": item["statistics"]["viewCount"],
            "likeCount": item["statistics"]["likeCount"],
            "commentCount": item["statistics"]["commentCount"],
            "duration": item["contentDetails"]["duration"],
        }
        for item in videos_response["items"]
    ]

    # Salvar os dados em JSON
    with open("f1_youtube.json", "w", encoding="utf-8") as f:
        json.dump(videos_response, f, ensure_ascii=False, indent=4)

    # Salvar os dados filtrados em JSON
    with open("f1_youtube_filtered.json", "w", encoding="utf-8") as f:
        json.dump(filtered_data, f, ensure_ascii=False, indent=4)

    print("Dados salvos em f1_youtube.json")
    print("Dados filtrados salvos em f1_youtube_filtered.json")

if __name__ == "__main__":
    main()