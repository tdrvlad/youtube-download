from pytube import YouTube, Search
import os
from googleapiclient.discovery import build
import dotenv
from typing import List, Dict, Optional
import isodate
from concurrent.futures import ThreadPoolExecutor, as_completed

dotenv.load_dotenv(".env")
DATA_DIR = os.getenv('DATA_DIR')


def merge_search_queries(search_queries_list_1: List[str], search_queries_list_2: List[str]):

    merged_search_queries =[]
    for query_1 in search_queries_list_1:
        for query_2 in search_queries_list_2:
            query = f"{query_1} {query_2}"
            merged_search_queries.append(query)
    return merged_search_queries


def get_videos_durations_and_tags(video_ids: List[str], api_key: str):
    """
    Fetch video durations from YouTube.
    Returns a dictionary mapping video IDs to their duration in seconds.
    """
    youtube = build('youtube', 'v3', developerKey=api_key)
    response = youtube.videos().list(
        part="contentDetails, snippet",
        id=",".join(video_ids)
    ).execute()

    video_tags = {}
    video_durations = {}
    for item in response.get("items", []):
        duration = isodate.parse_duration(item["contentDetails"]["duration"])
        video_durations[item["id"]] = int(duration.total_seconds())
        tags = item['snippet'].get('tags', [])
        video_tags[item["id"]] = tags

    return video_durations, video_tags


def check_tags(video_tags, target_tags):
    video_tags = [t.lower() for t in video_tags]
    for tag in target_tags:
        if tag in video_tags:
            return True
    return False


def search_youtube(search_query: str, download_limit: Optional[int] = None, min_length: Optional[int] = None, max_length: Optional[int] = None, target_tags: Optional[List[str]] = None) -> List[dict]:
    """
    Search YouTube and filter videos by duration.
    """
    # youtube = build('youtube', 'v3', developerKey=api_key)

    response = Search(search_query)
    initial_results = response.results
    results = initial_results

    if min_length is not None:
        results = [result for result in results if result.length > min_length]

    if max_length is not None:
        results = [result for result in results if result.length < max_length]

    if target_tags is not None:
        results = [result for result in results if check_tags(result.keywords, target_tags)]

    if download_limit is not None:
        results = results[:download_limit]

    urls = [result.watch_url for result in results]
    return urls


def download_videos(search_queries: dict, num_executors: int = 5, download_limit: Optional[int] = None, min_length: Optional[int] = None, max_length: Optional[int] = None, target_tags: Optional[List[str]] = None, download_dir: str = DATA_DIR):

    """
    Search YouTube for specific queries and download the results in a directory.
    Provide a valid Google API Key for the YouTube service.
    """

    DOWNLOADED_ITEMS = []

    for target, target_search_queries in search_queries.items():
        results_dir = os.path.join(download_dir, target)
        os.makedirs(results_dir, exist_ok=True)
        results = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_query = {executor.submit(search_youtube, search_query, download_limit, min_length, max_length,
                                               target_tags): search_query for search_query in target_search_queries}
            for future in as_completed(future_to_query):
                search_query = future_to_query[future]
                try:
                    urls = future.result()
                    print(f"Found {len(urls)} videos for search: {search_query}.")
                    results.extend(urls)
                except Exception as e:
                    print(f"Failed to search videos for query '{search_query}'. Error: {e}")

        print(f"\n\nDownloading {len(results)} videos to {results_dir}.\n\n")
        results = list(set(results))

        # Filter videos that were already downloaded
        results = [result for result in results if result not in DOWNLOADED_ITEMS]
        DOWNLOADED_ITEMS += results

        with ThreadPoolExecutor(max_workers=num_executors) as executor:
            future_to_url = {executor.submit(download_youtube_video, url, results_dir): url for url in results}
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    path = future.result()
                    if path:
                        print(f"Download completed and saved to {path}")
                except Exception as e:
                    print(f"Video download failed for {url}. Error: {e}")


def download_youtube_video(url, output_path="."):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video_path = stream.download(output_path=output_path)
        return video_path
    except Exception as e:
        print(f"Failed to download video segment from {url}. Error: {e}")
