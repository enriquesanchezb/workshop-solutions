import logging
import os
import re

from datasets import load_dataset

from src.transcribe import transcribe_audio

NUM_TESTS = 3
logger = logging.getLogger(__name__)


def insert_subdirectory_in_path(file_path):
    directory, filename = os.path.split(file_path)
    new_directory = os.path.join(directory, "train")
    new_file_path = os.path.join(new_directory, filename)
    return new_file_path


def remove_special_characters(text):
    return re.sub(r"[^a-zA-Z0-9\s]", "", text).lower().strip()


def test_transcribe_audio_with_dataset():
    dataset = load_dataset(
        "google/fleurs", "en_us", split="train[:10]", trust_remote_code=True
    )
    total = 0
    for sample in dataset.take(NUM_TESTS):
        path = insert_subdirectory_in_path(sample["path"])
        logger.info(f"Expected transcription: {sample['transcription']}")
        result = transcribe_audio(path)
        logger.info(f"Transcribed text: {result}")
        if remove_special_characters(result) == remove_special_characters(
            sample["transcription"]
        ):
            total += 1
    assert (total / NUM_TESTS) * 100 > 0.8
