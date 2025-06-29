#!/usr/bin/env python3
import os
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

def main():
    vid = VideoFileClip("clip.mp4")
    narr = AudioFileClip("narration.wav")

    bgm_path = os.getenv("BGM_PATH", "assets/bgm.mp3")
    bgm = AudioFileClip(bgm_path).volumex(0.3).audio_loop(duration=vid.duration)

    final_audio = CompositeAudioClip([bgm, narr])
    out = vid.set_audio(final_audio)
    out.write_videofile(
        "final.mp4",
        fps=24,
        codec="libx264",
        audio_codec="aac",
        preset="medium",
        threads=4,
        verbose=False,
        logger=None
    )
    print("✅ final.mp4 assembled")

if __name__ == "__main__":
    main()
