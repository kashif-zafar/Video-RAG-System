import os
import subprocess
from src.utils.config import VIDEO_DIR, AUDIO_DIR

def convert_videos_to_audio ():
    files = os.listdir(VIDEO_DIR)
    # print(files,sep='\n')

    for file in files:
        if not file.endswith(".mp4"):
            continue

        file_name = file.split('.mp4')[0]
        print(file_name)
        subprocess.run(["ffmpeg" , "-i" ,f"{VIDEO_DIR}/{file}", f"{AUDIO_DIR}/{file_name}.mp3"])

if __name__ == "__main__":
    convert_videos_to_audio()
