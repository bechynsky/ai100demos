import json, os, requests
from pprint import pprint

subscription_key = os.environ.get('CV_KEY')
endpoint = os.environ.get("CV_ENDPOINT")

face_api_url = endpoint + 'face/v1.0/detect'

image_url = 'https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/faces.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
	'detectionModel': 'detection_01',
	'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    'returnFaceId': 'true'
}

response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})
pprint(response.json())