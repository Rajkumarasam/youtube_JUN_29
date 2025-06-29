#!/usr/bin/env python3
from TTS.api import TTS
import os

def main():
    # you can change this to any Coqui-supported en_US model
    model_name = os.getenv("TTS_MODEL", "tts_models/en/ljspeech/tacotron2-DDC")
    # load the TTS model (cpu by default; add gpu=True if you have a GPU runner)
    tts = TTS(model_name, progress_bar=False, gpu=False)

    # read your script
    with open("script.txt", "r") as f:
        text = f.read().strip()

    # generate WAV
    tts.tts_to_file(text=text, file_path="narration.wav")
    print("✅ narration.wav generated")

if __name__ == "__main__":
    main()
