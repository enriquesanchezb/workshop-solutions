"""
This script converts text to speech using the Google Text-to-Speech (gTTS) API.
Example usage:
    python text_to_speech.py -t "Hello, how are you?" -o hello.mp3
    python text_to_speech.py -f text.txt -o output.mp3
"""

import argparse
import sys
import time

from colorama import Fore, Style
from gtts import gTTS
from tqdm import tqdm


def text_to_speech(text: str, filename: str) -> None:
    """Convert text to speech and save the audio file."""
    print(Fore.CYAN + "Starting text-to-speech conversion..." + Style.RESET_ALL)

    # Simulate processing with a progress bar
    for _ in tqdm(range(10), desc="Converting Text", file=sys.stdout):
        time.sleep(0.2)  # Simulated delay for demonstration

    tts = gTTS(text=text, lang="en", slow=False)
    tts.save(filename)
    print(Fore.GREEN + f"Audio file created as {filename}" + Style.RESET_ALL)


def read_text_file(file_path: str) -> str:
    """Read text from a file."""
    with open(file_path, "r") as file:
        return file.read()


if __name__ == "__main__":
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Convert text to speech.")
    parser.add_argument(
        "-t", "--text", type=str, help="Direct input text to convert to speech."
    )
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="File path for a file containing text to convert to speech.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="output.mp3",
        help="Output file name for the audio file.",
    )

    args = parser.parse_args()

    # Input text handling
    input_text = ""
    if args.text:
        input_text = args.text
    elif args.file:
        input_text = read_text_file(args.file)
    else:
        print(
            Fore.RED
            + "No input text or file provided. Please use the -t or -f option."
            + Style.RESET_ALL
        )
        sys.exit(1)

    # Convert text to speech
    text_to_speech(input_text, args.output)
