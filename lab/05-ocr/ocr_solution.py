import io
import os

from typing import Any, Tuple
from dotenv import load_dotenv

# Computer Vision modules
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials


load_dotenv()

cog_endpoint = os.getenv("COG_SERVICE_ENDPOINT")
cog_key = os.getenv("COG_SERVICE_KEY")


def get_texts(image_data: bytes) -> Tuple[str, Any]:
    # Instantiate Cognitive Services credentials using `cog_key`
    credentials = CognitiveServicesCredentials(cog_key)

    # Instantiate Computer Vision Client using `cog_endpoint` and `credentials` variables
    client = ComputerVisionClient(cog_endpoint, credentials)

    # Use a binary stream generator from the image data
    image_stream = io.BytesIO(image_data)

    # Analyze the image stream to extract all printed texts
    results = client.recognize_printed_text_in_stream(image_stream)

    # Extract the detected text language
    language = results.language

    # Extract all the detected texts data (position, text)
    texts = [
        dict(
            position=tuple(map(int, r.bounding_box.split(","))),
            text=" ".join([w.text for l in r.lines for w in l.words]),
        )
        for r in results.regions
    ]

    return language, texts
