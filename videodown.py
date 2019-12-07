import os
import sys
import pyfiglet
import youtube_dl
from colorama import Fore

save_dir = "./videos/"
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
outtmpl = "%(title)s.%(ext)s"

ydl_opts = {
    "outtmpl": save_dir + outtmpl,
}


def download(url):
    print("> Downloading ...")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print(">" + Fore.LIGHTGREEN_EX + " Download complete!")


if __name__ == "__main__":
    try:
        figlet = pyfiglet.figlet_format("YDL Video")
        print(Fore.LIGHTBLUE_EX + figlet)
        print("Youtube, niconico, etc...\n" + Fore.RESET)
        url = input("> Enter url : ")
        while not url:
            print(">" + Fore.RED + " Not entered" + Fore.RESET)
            url = input("> Enter url : ")
        download(url)
    except KeyboardInterrupt:
        print("\n>" + Fore.GREEN + " Exit program")
        sys.exit()