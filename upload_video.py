#!/usr/bin/env python3
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def main():
    token = os.environ["YT_ACCESS_TOKEN"]
    creds = Credentials(token)
    youtube = build("youtube", "v3", credentials=creds)

    title       = os.getenv("VIDEO_TITLE", "Kids Learning Video")
    description = os.getenv("VIDEO_DESCRIPTION", "Learn the alphabet with fun animations!")
    privacy     = os.getenv("VIDEO_PRIVACY", "public")

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["kids","education","alphabet"],
                "categoryId": "27"
            },
            "status": {"privacyStatus": privacy}
        },
        media_body=MediaFileUpload("final.mp4", chunksize=-1, resumable=True)
    )
    response = request.execute()
    print(f"✅ Uploaded video ID: {response['id']}")

if __name__ == "__main__":
    main()
