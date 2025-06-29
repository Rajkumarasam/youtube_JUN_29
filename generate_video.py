#!/usr/bin/env python3
import os, requests

def main():
    hf_token = os.environ["HF_TOKEN"]
    model_id = os.getenv("HF_MODEL", "YourUser/HunyuanVideo-GGUF")
    with open("script.txt", "r") as f:
        prompt = f.read()

    headers = {"Authorization": f"Bearer {hf_token}"}
    payload = {
        "inputs": prompt,
        "options": {"wait_for_model": True},
        "parameters": {
            "resolution": "480p",
            "duration_s": 3
        }
    }
    res = requests.post(
        f"https://api-inference.huggingface.co/models/{model_id}",
        headers=headers,
        json=payload
    )
    res.raise_for_status()
    with open("clip.mp4", "wb") as vf:
        vf.write(res.content)
    print("✅ clip.mp4 generated")

if __name__ == "__main__":
    main()
