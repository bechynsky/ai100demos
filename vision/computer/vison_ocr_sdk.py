import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

from dotenv import load_dotenv

load_dotenv()

key = os.environ.get("CV_KEY")
endpoint = os.environ.get("CV_ENDPOINT")
location = os.environ.get("CV_LOCATION")

client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

result = client.analyze(
    image_url="https://aka.ms/azsdk/image-analysis/sample.jpg",
    visual_features=[VisualFeatures.READ]
)

print(result.read.blocks[0].lines)