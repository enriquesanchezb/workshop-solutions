# Branch: 3-Emotion-DetectionWorkshop instructions

Welcome to the `3-emotion-detection` branch of our AI Testing workshop! This branch focuses on a sentiment analysis app that analyzes the sentiment from your voice. Your task is to test and ensure its functionality.

## Installation

Before you begin, make sure Python and Poetry are installed. Then, set up the project dependencies:

1. **Install dependencies**
Navigate to the project directory and run:

```bash
poetry install
```
2. **Troubleshooting TensorFlow Installation:**
Depending on your OS you can have some problems installing `Tensorflow` or `tf-keras`. If it happens, review how to install Tensorflow [here](https://www.tensorflow.org/install)

## Running the app

To start the sentiment analysis app, execute the following command:

```bash
poetry run python app.py
```

You should see the following message indicating the app is running locally:

```bash
> poetry run python app.py
Running on local URL:  http://127.0.0.1:7860

To create a public link, set `share=True` in `launch()`.
```

Access the app via `http://127.0.0.1:7860`.

## Running Test Cases

Run the existing automated tests with this command:

```bash
poetry run pytest
```

## Exercises

**Exercise 1:** 
The test file `/tests/test_sentiment.py` is currently not functioning as expected. Review and correct the errors to make it operational.

**Exercise 2:**
The file `/tests/test_transcribe.py` requires fixes. Utilize the sample audio file located in `/tests/samples` to test and ensure it properly transcribes the audio.

## Support
If you run into any issues or have questions, please contact the workshop organizers.

--- 
Happy testing! Discover how to enhance and debug testing processes for sentiment analysis applications!

---