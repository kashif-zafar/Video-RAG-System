import os
import subprocess
from src.utils.config import VIDEO_DIR, AUDIO_DIR, TRANSCRIPT_DIR
files = os.listdir(VIDEO_DIR)
# print(files,sep='\n')

for file in files:
    file_name = file.split('.mp4')[0]
    print(file_name)
    subprocess.run(["ffmpeg" , "-i" ,f"{VIDEO_DIR}/{file}", f"{AUDIO_DIR}/{file_name}.mp3"])
