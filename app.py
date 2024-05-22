import gradio as gr

from src.sentiment import analyze_sentiment
from src.transcribe import transcribe_audio

TITLE = """<h1 align="center">🎤 Emotion Detection 💬</h1>"""

EMOJI_MAPPING = {
    "disappointment": "😞",
    "sadness": "😢",
    "annoyance": "😠",
    "neutral": "😐",
    "disapproval": "👎",
    "realization": "😮",
    "nervousness": "😬",
    "approval": "👍",
    "joy": "😄",
    "anger": "😡",
    "embarrassment": "😳",
    "caring": "🤗",
    "remorse": "😔",
    "disgust": "🤢",
    "grief": "😥",
    "confusion": "😕",
    "relief": "😌",
    "desire": "😍",
    "admiration": "😌",
    "optimism": "😊",
    "fear": "😨",
    "love": "❤️",
    "excitement": "🎉",
    "curiosity": "🤔",
    "amusement": "😄",
    "surprise": "😲",
    "gratitude": "🙏",
    "pride": "🦁",
}


def get_sentiment_emoji(sentiment: str) -> str:
    """Returns the emoji corresponding to the sentiment"""
    return EMOJI_MAPPING.get(sentiment, "")


def display_sentiment_results(sentiment_results: dict) -> str:
    """Returns the sentiment analysis results as a string"""
    sentiment_text = ""
    for sentiment, _ in sentiment_results.items():
        emoji = get_sentiment_emoji(sentiment)
        sentiment_text += f"{sentiment} {emoji}\n"
    return sentiment_text


def get_ouput(audio_file: str, audio_file_uploaded: str) -> (str, str):
    """Returns the transcribed text and the sentiment analysis results"""
    if audio_file_uploaded:
        audio_file = audio_file_uploaded

    try:
        text = transcribe_audio(audio_file)
        sentiment = analyze_sentiment(text)
        return text, display_sentiment_results(sentiment)
    except Exception as e:
        print(f"Error in transcribe_audio: {e}")
        return "", "Error in transcription."


def main():
    """Main function"""
    block = gr.Blocks()
    with block:
        gr.HTML(TITLE)

        with gr.Group():
            audio_input = gr.Audio(
                sources=["microphone"], type="filepath", elem_id="audio_input"
            )
            upload_audio = gr.UploadButton(
                label="Upload Audio",
                file_types=["audio"],
                type="filepath",
                elem_id="upload_audio",
            )
            output_text = gr.Textbox(label="Transcription", elem_id="output_text")
            emotion_output = gr.Textbox(
                label="Emotion Analysis", elem_id="emotion_output"
            )

            gr.Interface(
                fn=get_ouput,
                inputs=[audio_input, upload_audio],
                outputs=[output_text, emotion_output],
                title="Get the text and the sentiment",
                description="Upload an audio file and hit the 'Submit'\
                                  button",
            )
    block.launch()


if __name__ == "__main__":
    main()
