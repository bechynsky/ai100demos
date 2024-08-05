import os
import sys
import requests
import json
from io import BytesIO
from pprint import pprint

from dotenv import load_dotenv

load_dotenv()

subscription_key = os.environ.get('CV_KEY')
endpoint = os.environ.get("CV_ENDPOINT")

# https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/how-to/call-analyze-image-40?pivots=programming-language-rest-api
analyze_url = endpoint + "/computervision/imageanalysis:analyze?api-version=2024-02-01&features=tags"

# Set image_path to the local path of an image that you want to analyze.
# Sample images are here, if needed:
# https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/ComputerVision/Images

sample_file_path = os.environ.get("SAMPLE_FILE")


# Read the image into a byte array
image_data = open(sample_file_path, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}

response = requests.post(
    analyze_url, 
    headers=headers, 
    data=image_data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
pprint(response.json())
