# YouTube Playlist Downloader

A Python script to download videos from a YouTube playlist using `yt-dlp`. The script allows users to specify the playlist URL and the folder where the videos will be saved. 

## Features

- Downloads all videos in a YouTube playlist.
- Saves videos with their playlist index and title for organized storage.
- Supports merging of video and audio streams using `ffmpeg`.
- Automatically creates the target folder if it does not exist.

## Prerequisites

Before running the script, ensure you have the following installed:

- **Python 3.10+**
- **yt-dlp** (for downloading YouTube videos)
- **ffmpeg** (for merging video and audio streams)

### Installing Dependencies

Install the required Python library:
```bash
pip install yt-dlp
```

Install `ffmpeg`:

- On **macOS**:
  ```bash
  brew install ffmpeg
  ```

- On **Ubuntu/Linux**:
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

- On **Windows**:
  Download the latest release from [ffmpeg.org](https://ffmpeg.org/), extract the files, and add the `bin` directory to your system's PATH.

## How to Use

1. Clone or download the script to your local machine.
2. Open a terminal and navigate to the script directory.
3. Run the script:
   ```bash
   python playlist_downloader.py
   ```
4. Follow the prompts:
   - Enter the URL of the YouTube playlist.
   - Enter the name of the folder where videos will be saved.

## Example Usage

```plaintext
Enter YouTube Playlist URL: ✨https://www.youtube.com/playlist?list=PLabc123xyz
Enter folder name to save videos: MyPlaylist
```

The videos will be downloaded into the `MyPlaylist` folder.

## Output File Structure

The downloaded videos are saved with their playlist index and title:
```
MyPlaylist/
├── 01 - Video Title 1.mp4
├── 02 - Video Title 2.mp4
├── 03 - Video Title 3.mp4
...
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for providing an amazing video downloading library.
- [ffmpeg](https://ffmpeg.org/) for handling video and audio stream merging.
```