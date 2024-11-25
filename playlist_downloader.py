# import os
# from yt_dlp import YoutubeDL
#
# link = input("Enter YouTube Playlist URL: ✨")
#
# folder_name = input("Enter folder name to save videos: ")
# os.makedirs(folder_name, exist_ok=True)
#
# options = {
#     'outtmpl': os.path.join(folder_name, '%(playlist_index)s - %(title)s.%(ext)s'),
#     'format': 'best',
#     'noplaylist': False,
#     'socket_timeout': 30,
#     'retries': 5,
# }
#
# with YoutubeDL(options) as ydl:
#     ydl.download([link])

import os
from yt_dlp import YoutubeDL


def get_downloaded_videos(folder):
    """Get the list of downloaded videos in the folder."""
    downloaded_files = os.listdir(folder)
    downloaded_videos = set(
        os.path.splitext(file)[0] for file in downloaded_files if os.path.isfile(os.path.join(folder, file)))
    return downloaded_videos


def download_youtube_playlist():
    link = input("Enter YouTube Playlist URL: ✨ ")
    folder_name = input("Enter folder name to save videos: ")
    os.makedirs(folder_name, exist_ok=True)

    # Retrieve the already downloaded videos
    downloaded_videos = get_downloaded_videos(folder_name)

    options = {
        'outtmpl': os.path.join(folder_name, '%(playlist_index)s - %(title)s.%(ext)s'),
        'format': 'best',
        'noplaylist': False,
        'socket_timeout': 30,
        'retries': 5,
        'download_archive': os.path.join(folder_name, '.downloaded_videos'),  # Prevent re-downloading
        'progress_hooks': [lambda d: print(f"Downloaded: {d.get('filename')}") if d['status'] == 'finished' else None],
    }

    print(f"Found {len(downloaded_videos)} videos already downloaded. Continuing with the rest...\n")

    with YoutubeDL(options) as ydl:
        ydl.download([link])


if __name__ == "__main__":
    download_youtube_playlist()
