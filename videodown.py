import os
import sys
import subprocess




"""
Usage:
    1:youtube-dlを入手(https://youtube-dl.org/)　または pip install youtube-dlをする
    2:FFmpegを入手(https://www.ffmpeg.org/)
    3:このファイルと同階層上にffmpeg.exeを置く
    4:ファイルの実行(python videodown.py [youtube video url])
"""




class Downloader:

    def __init__(self):
        self.save_dir = "./videos/"
        self.outtmpl = "%(title)s.%(ext)s"


    def download(self, url):
        command = (
            "youtube-dl",
            "--format",
            "137+140",
            "--merge-output-format",
            "mp4",
            "--output",
            self.save_dir+self.outtmpl,
            url
        )
        with subprocess.Popen(command) as process:
            process.wait()
            print("youtube-dl return code:", process.returncode, "\ncomplete")


    def make_save_dir(self):
        if not os.path.exists(self.save_dir):
            os.mkdir(self.save_dir)




def main():
    downlaoder = Downloader()
    downlaoder.make_save_dir()
    try:
        downlaoder.download(url=sys.argv[1])
    except IndexError:
        print("Enter the URL of the video you want to download in the argument")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        raise e
