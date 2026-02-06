import yt_dlp
import os

def download_video(url, output_path='./downloads'):
    try:
        # Ensure the output directory exists
        os.makedirs(output_path, exist_ok=True)

        # Configuration for yt-dlp
        # '%(title)s.%(ext)s' automatically names the file after the video title
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best', 
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Starting download for: {url}")
            ydl.download([url])
            
        print("Download completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)