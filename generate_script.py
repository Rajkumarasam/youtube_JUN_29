#!/usr/bin/env python3
import subprocess, argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model",
        default="llama.cpp/models/mistral-7b.gguf",
        help="Path to your GGUF llama model"
    )
    parser.add_argument(
        "--prompt",
        default="Write a bright, rhyming 30-second animated alphabet video for kids about the letter A.",
        help="Story prompt"
    )
    args = parser.parse_args()

    cmd = [
        "llama.cpp/main",
        "-m", args.model,
        "-p", args.prompt,
        "--temp", "0.8",
        "--repeat_penalty", "1.1"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    script = result.stdout.strip()
    with open("script.txt", "w") as f:
        f.write(script)
    print("✅ script.txt generated")

if __name__ == "__main__":
    main()
