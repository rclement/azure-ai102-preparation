import os
import requests

from typing import Tuple
from urllib.parse import urljoin
from dotenv import load_dotenv


load_dotenv()


cog_endpoint = os.getenv("COG_SERVICE_ENDPOINT")
cog_key = os.getenv("COG_SERVICE_KEY")


def detect_language(text: str) -> Tuple[str, float]:
    url = urljoin(cog_endpoint, "/text/analytics/v3.0/languages")
    headers = {
        "Ocp-Apim-Subscription-Key": cog_key
    }

    # fill the request body parameters with the input text
    params = ...

    response = requests.post(url, headers=headers, json=params)
    response.raise_for_status()
    data = response.json()

    # find the detected language for the document from the JSON data response
    detected_language = ...
    # find the language name from the detected language
    language = ...
    # find the language confidence score from the detected language
    confidence = ...

    return language, confidence


if __name__ == "__main__":
    text = input("Enter text: ")
    language, confidence = detect_language(text)
    print(f"Detected language {language} with {confidence * 100}% confidence")
