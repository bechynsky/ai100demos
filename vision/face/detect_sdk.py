import os

from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.face import FaceClient
from azure.ai.vision.face.models import (
    FaceDetectionModel,
    FaceRecognitionModel,
    FaceAttributeTypeDetection03,
    FaceAttributeTypeRecognition04,
)

from dotenv import load_dotenv
load_dotenv()

key = os.environ.get("CV_KEY")
endpoint = os.environ.get("CV_ENDPOINT")
location = os.environ.get("CV_LOCATION")

sample_file_path = os.environ.get("SAMPLE_FILE")

with open(sample_file_path, "rb") as fd:
    file_content = fd.read()

# https://learn.microsoft.com/en-us/python/api/overview/azure/ai-vision-face-readme?view=azure-python-preview
face_client = FaceClient(endpoint, AzureKeyCredential(key))

result = face_client.detect(file_content, 
                    detection_model=FaceDetectionModel.DETECTION_03, 
                    recognition_model=FaceRecognitionModel.RECOGNITION_04,
                    return_recognition_model=True,
                    # If you change to True, you will get face ID in result and you need approval for it
                    return_face_id=False,
                    return_face_attributes=[
                        FaceAttributeTypeDetection03.HEAD_POSE,
                        FaceAttributeTypeDetection03.MASK,
                        FaceAttributeTypeRecognition04.QUALITY_FOR_RECOGNITION,
                    ])

print(result)