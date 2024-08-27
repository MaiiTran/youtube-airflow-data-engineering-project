import pandas as pd 
import json
from datetime import datetime
import s3fs 
import os 
from googleapiclient.discovery import build
 
def run_youtube_etl():
    api_key = os.getenv("YOUTUBE_KEY")
    # video_id 
    video_id = 'M4n_hs_XmJs'

    # empty list for storing reponse
    reponses = []
    # empty list for storing reply   
    replies_count = []
 
    # creating youtube resource object
    youtube = build('youtube', 'v3',
                    developerKey=api_key)
 
    # retrieve youtube video results
    video_response = youtube.commentThreads().list(
        part = 'snippet,replies',
        videoId = video_id,
        ).execute()
    
    while video_response:
        for item in video_response['items']:
            reponse = item['snippet']['topLevelComment']['snippet']['textDisplay']
            reponses.append(reponse)

            reply_count = item['snippet']['totalReplyCount']  
            replies_count.append(reply_count)
        
        # Repeat for get data from other pages 
        if 'nextPageToken' in video_response:
            video_response = youtube.commentThreads().list(
            part = 'snippet,replies',
            videoId = video_id,
            pageToken = video_response['nextPageToken']
            ).execute()
        else:
            break

    # dict of lists
    df = {'reponse': reponses, 'reply_count': replies_count}
    # convert dict to DataFrame 
    df = pd.DataFrame(df)
    df.to_csv("youtube_video.csv")

run_youtube_etl()