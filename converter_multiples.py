from pytubefix import YouTube
from pytubefix.cli import on_progress



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
    filename = 'paste_links_here.txt'
    file = open(filename)
    for i in range(count_lines(filename)):
        mp3_convert(file.readline())
    file.close()
    file = open(filename,"w")
    file.close()
    print("download_finish")

if __name__ == "__main__":
    main()