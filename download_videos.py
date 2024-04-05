from pytube import YouTube
import os
from googleapiclient.discovery import build
import dotenv
from typing import List, Dict
import isodate

dotenv.load_dotenv(".env")
GOOGLE_API_KEY = os.getenv("API_KEY")
DATA_DIR = os.getenv('DATA_DIR')


def get_video_durations(video_ids: List[str], api_key: str) -> Dict[str, int]:
    """
    Fetch video durations from YouTube.
    Returns a dictionary mapping video IDs to their duration in seconds.
    """
    youtube = build('youtube', 'v3', developerKey=api_key)
    response = youtube.videos().list(
        part="contentDetails",
        id=",".join(video_ids)
    ).execute()

    video_durations = {}
    for item in response.get("items", []):
        duration = isodate.parse_duration(item["contentDetails"]["duration"])
        video_durations[item["id"]] = int(duration.total_seconds())

    return video_durations


def search_youtube(search_query: str, api_key: str, download_limit: int = 25, min_length: int = 0, max_length: int = 60) -> List[dict]:
    """
    Search YouTube and filter videos by duration.
    """
    youtube = build('youtube', 'v3', developerKey=api_key)

    search_response = youtube.search().list(
        q=search_query,
        part='id,snippet',
        maxResults=download_limit,
        type='video'
    ).execute()

    video_ids = [item['id']['videoId'] for item in search_response.get('items', [])]
    durations = get_video_durations(video_ids, api_key)

    results = []
    for item in search_response.get('items', []):
        video_id = item['id']['videoId']
        if durations.get(video_id, 0) >= min_length and durations.get(video_id, 0) <= max_length:
            results.append({
                'url': f"https://www.youtube.com/watch?v={video_id}",
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'channel': item['snippet']['channelTitle'],
                'duration': durations[video_id]  # Optional, if you want to keep track of duration
            })
    return results


def download_videos(search_queries: dict, api_key: str = GOOGLE_API_KEY, download_limit: int = 10, download_dir: str = DATA_DIR):
    """
    Search YouTube for specific queries and download the results in a directory.
    Provide a valid Google API Key for the YouTube service.
    """

    for target, target_search_queries in search_queries.items():
        results_dir = os.path.join(download_dir, target)
        os.makedirs(results_dir, exist_ok=True)
        results = []
        for search_query in target_search_queries:
            search_results = search_youtube(search_query, api_key=api_key, download_limit=download_limit)
            print(f"Found {len(search_results)} videos for search: {search_query}.")
            results.extend(search_results)
        print(f"Downloading {len(results)} videos to {results_dir}.")
        for result in results:
            download_youtube_video(result['url'], output_path=results_dir)


def download_youtube_video(url, output_path="."):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video_path = stream.download(output_path=output_path)
        return video_path
    except Exception as e:
        print(f"Failed to download video segment from {url}. Error: {e}")
