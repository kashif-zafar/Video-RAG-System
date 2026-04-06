import whisper
import json
import os
from src.utils.config import  AUDIO_DIR, TRANSCRIPT_DIR
model = whisper.load_model("large-v2")

audios = os.listdir(AUDIO_DIR)

for audio in audios: 
    if("_" in audio):
        number = audio.split("_")[0]
        title = audio.split("_")[1][:-4]
        print(number, title)
        result = model.transcribe(audio = f"{AUDIO_DIR}/{audio}", 
        
                              language="en",
                              task="translate",
                              word_timestamps=False )
        
        chunks = []
        for segment in result["segments"]:
            chunks.append({"number": number, "title":title, "start": segment["start"], "end": segment["end"], "text": segment["text"]})
        
        chunks_with_metadata = {"chunks": chunks, "text": result["text"]}

        with open(os.path.join(TRANSCRIPT_DIR, f"{title}.json"), "w") as f:
            json.dump(chunks_with_metadata,f)


