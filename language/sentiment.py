import os
import requests

# pprint is used to format the JSON response
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

subscription_key = os.environ.get("CV_KEY")
endpoint = os.environ.get("CV_ENDPOINT")


language_api_url = endpoint + "/language/:analyze-text?api-version=2023-11-15-preview"


documents = {
    "kind": "SentimentAnalysis",
    "parameters": {
        "modelVersion": "latest"
    },
    "analysisInput":{
         "documents": [
          {"language": "en", "id": "1", "text": "The restaurant had great food and our waiter was friendly."},
          {"language": "en", "id": "2", "text": "The restaurant had strange food and our waiter was super slow."},
          {"language": "cs", "id": "3", "text": "Večeři jsem si užil."}
        ]
    }
}


headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()
pprint(languages)