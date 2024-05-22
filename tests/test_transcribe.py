import os
import random
import re


import pytest
from datasets import load_dataset
from gtts import gTTS

from src.transcribe import transcribe_audio

dataset = load_dataset("go_emotions", "simplified", split="train")
NUM_TESTS = 3


def remove_special_characters(text):
    return re.sub(r"[^a-zA-Z0-9\s]", "", text).lower().strip()


@pytest.fixture
def audio_file():
    file_path = os.path.join("/tmp", "test.mp3")
    yield file_path
    os.remove(file_path)


@pytest.mark.parametrize(
    "sample",
    [dataset[random.randint(0, len(dataset) - 1)] for _ in range(NUM_TESTS)],
)
def test_transcribe_audio(audio_file, sample):
    text = sample["text"]
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save(audio_file)
    assert remove_special_characters(
        transcribe_audio(audio_file)
    ) == remove_special_characters(text)
