import os

from typing import Tuple
from dotenv import load_dotenv

# Text Analytics module
from azure.ai.textanalytics import TextAnalyticsClient

# Azure Key Credentials module
from azure.core.credentials import AzureKeyCredential


load_dotenv()

cog_endpoint = os.getenv("COG_SERVICE_ENDPOINT")
cog_key = os.getenv("COG_SERVICE_KEY")


def get_sentiment(text: str) -> Tuple[str, str, float, float, float]:
    # Instantiate Azure Key Credential using `cog_key` variable
    credential = AzureKeyCredential(cog_key)

    # Instantiate Text Analytics Client using `cog_endpoint` and `credential` variables
    client = TextAnalyticsClient(endpoint=cog_endpoint, credential=credential)

    # Find out the language of the text
    results = client.detect_language([text])
    detected_language = results[0].primary_language

    # Prepare documents with detected language
    documents = [{"id": 1, "text": text, "language": detected_language.iso6391_name}]

    # Analyze the sentiment of the documents
    results = client.analyze_sentiment(documents)

    # Extract results
    sentiment = results[0].sentiment
    positive = results[0].confidence_scores.positive
    neutral = results[0].confidence_scores.neutral
    negative = results[0].confidence_scores.negative

    return detected_language.name, sentiment, positive, neutral, negative


if __name__ == "__main__":
    text = input("Text to analyze: ")
    language, sentiment, positive, neutral, negative = get_sentiment(text)
    print(f"Detected {language} text with {sentiment} sentiment")
    print(f"({positive * 100}% positive, {neutral * 100}% neutral, {negative * 100}% negative)")
