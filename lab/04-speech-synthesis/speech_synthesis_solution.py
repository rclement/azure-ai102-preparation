import os

from dotenv import load_dotenv

# Speech modules
from azure.cognitiveservices import speech


load_dotenv()

cog_endpoint = os.getenv("COG_SERVICE_ENDPOINT")
cog_key = os.getenv("COG_SERVICE_KEY")
cog_region = os.getenv("COG_REGION")


def speech_synthesis(text: str) -> None:
    # Instantiate Cognitive Services credentials using `cog_key`
    speech_config = speech.SpeechConfig(cog_key, cog_region)
    speech_config.speech_synthesis_voice_name = "en-GB-RyanNeural"
    speech_synthesizer = speech.SpeechSynthesizer(speech_config)
    speak = speech_synthesizer.speak_text_async(text).get()
    if speak.reason != speech.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)


if __name__ == "__main__":
    text = input("Text: ")
    speech_synthesis(text)
