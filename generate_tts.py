#!/usr/bin/env python3
import os
from orpheus_tts import OrpheusModel

def main():
    model_name = os.getenv("ORPHEUS_MODEL", "canopylabs/orpheus-tts-0.1-finetune-prod")
    voice = os.getenv("ORPHEUS_VOICE", "tara")
    with open("script.txt", "r") as f:
        text = f.read()

    tts = OrpheusModel(model_name=model_name)
    audio_chunks = tts.generate_speech(prompt=text, voice=voice)

    with open("narration.wav", "wb") as wf:
        for chunk in audio_chunks:
            wf.write(chunk)
    print("✅ narration.wav generated")

if __name__ == "__main__":
    main()
