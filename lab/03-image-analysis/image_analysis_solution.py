import io
import os

from typing import Any
from dotenv import load_dotenv

# Computer Vision modules
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


load_dotenv()

cog_endpoint = os.getenv("COG_SERVICE_ENDPOINT")
cog_key = os.getenv("COG_SERVICE_KEY")


def get_faces(image_data: bytes) -> Any:
    # Instantiate Cognitive Services credentials using `cog_key`
    credentials = CognitiveServicesCredentials(cog_key)

    # Instantiate Computer Vision Client using `cog_endpoint` and `credentials` variables
    client = ComputerVisionClient(cog_endpoint, credentials)

    # Use a binary stream generator from the image data
    image_stream = io.BytesIO(image_data)

    # Select the visual features to extract faces data
    features = [VisualFeatureTypes.faces]

    # Analyze the image stream to extract the selected features
    analysis = client.analyze_image_in_stream(image_stream, features)

    # Extract faces features
    faces = [
        dict(
            age=f.age,
            gender=f.gender.value,
            position=dict(
                left=f.face_rectangle.left,
                top=f.face_rectangle.top,
                width=f.face_rectangle.width,
                height=f.face_rectangle.height,
            )
        )
        for f in analysis.faces
    ]

    return faces
