
from celery import shared_task
import requests
from .models import Video

@shared_task
def fetch_youtube_videos():
    API_KEY = 'AIzaSyBoNHfSyCy69f5rCBDrHnl_esVL5cuI2bE'
    CHANNEL_ID = 'UC8f-tYo2-VpOATa2_tPiIEg'
    url = f'https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={CHANNEL_ID}&part=snippet,id&order=date&maxResults=20'

    response = requests.get(url)
    videos = response.json().get('items', [])

    for video in videos:
        video_id = video['id']['videoId']
        snippet = video['snippet']
        title = snippet['title']
        description = snippet['description']
        published_at = snippet['publishedAt']
        embed_url = f'https://www.youtube.com/embed/{video_id}'

        if not Video.objects.filter(slug=video_id).exists():
            Video.objects.create(
                slug=video_id,
                title=title,
                description=description,
                embed_url=embed_url,
                published_at=published_at,
                is_recent=True,
            )
