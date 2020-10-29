import os
import sys
import requests
import json
from io import BytesIO
from pprint import pprint

subscription_key = os.environ.get('CV_KEY')
endpoint = os.environ.get("CV_ENDPOINT")

analyze_url = endpoint + "vision/v3.0/analyze"

# Set image_path to the local path of an image that you want to analyze.
# Sample images are here, if needed:
# https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/ComputerVision/Images
# image_path = "c:/Users/stbechyn/Documents/AI-100-Design-Implement-Azure-AISol/Lab2-Implement_Computer_Vision/sample_images/Analysis_9.jpg"
# image_path = "C:/Users/stbechyn/Pictures/20201008_133255.jpg"
image_path = "C:/Users/stbechyn/Pictures/20201016_085235.jpg"

# Read the image into a byte array
image_data = open(image_path, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}
params = {'visualFeatures': 'Categories,Description,Brands'}
#params = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(
    analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
pprint(response.json())
