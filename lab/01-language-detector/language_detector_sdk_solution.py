import os

from typing import Tuple
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv


load_dotenv()


cog_endpoint = os.getenv("COG_SERVICE_ENDPOINT")
cog_key = os.getenv("COG_SERVICE_KEY")


def detect_language(text: str) -> Tuple[str, float]:
    credential = AzureKeyCredential(cog_key)
    client = TextAnalyticsClient(endpoint=cog_endpoint, credential=credential)

    # fill the request body parameters with the input text
    documents = [text]

    results = client.detect_language(documents=documents)

    # find the detected language for the document from the results
    detected_language = results[0].primary_language
    # find the language name from the detected_language
    language = detected_language.name
    # find the language confidence score from the detected_language
    confidence = detected_language.confidence_score

    return language, confidence


if __name__ == "__main__":
    text = input("Enter text: ")
    language, confidence = detect_language(text)
    print(f"Detected language {language} with {confidence * 100}% confidence")
