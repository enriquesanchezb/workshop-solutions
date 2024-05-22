import os

from playwright.sync_api import expect, sync_playwright


def test_emotion_detection_app():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(
            headless=False
        )  # Set headless=False to see the browser interaction
        page = browser.new_page()

        page.goto("http://127.0.0.1:7860")
        with page.expect_file_chooser() as fc_info:
            page.get_by_text("Upload Audio").click()
        file_chooser = fc_info.value
        file_path = os.path.join(os.path.dirname(__file__), "samples", "test.mp3")
        file_chooser.set_files(file_path)

        page.click("text='Submit'")

        expect(page.get_by_label("Transcription")).to_have_value(" This is a test.")
        expect(page.get_by_label("Emotion Analysis")).to_have_value("neutral 😐\n")

        browser.close()


if __name__ == "__main__":
    test_emotion_detection_app()
