import sys
import youtube_dl

def main(url):
    ydl = youtube_dl.YoutubeDL({'outtmpl' : '%(title)s.%(ext)s'})
    ydl.add_default_info_extractors()
    result = ydl.extract_info(url, download=True)

if __name__ == "__main__":
    main(sys.argv[1])
