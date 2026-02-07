from pathlib import Path
from openai import OpenAI

client = OpenAI()

def text_to_speech(text: str, output_file: str):
    output_path = Path(output_file)

    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text
    )

    with open(output_path, "wb") as f:
        f.write(response.read())
