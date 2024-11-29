from pytubefix import YouTube
from pytubefix.cli import on_progress
import fetch_ui


def mp3_convert(link):
    yt = YouTube(link,on_progress_callback = on_progress)
    print(yt.title)
    ys = yt.streams.get_audio_only()
    ys.download(output_path= "",mp3 = True)

def count_lines(filename):
    with open(filename,'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        return line_count

def main():
  
    url = fetch_ui.capture_ui()
    mp3_convert(url)
    print("download_finish")

if __name__ == "__main__":
    main()