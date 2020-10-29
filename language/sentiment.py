import os
import requests

# pprint is used to format the JSON response
from pprint import pprint

subscription_key = os.environ.get("CV_KEY")
endpoint = os.environ.get("CV_ENDPOINT")


language_api_url = endpoint + "text/analytics/v3.0/sentiment"

documents = {
  "documents": [
    {"language": "en", "id": "1", "text": "The restaurant had great food and our waiter was friendly."},
    {"language": "en", "id": "2", "text": "The restaurant had strange food and our waiter was super slow."},
    {"language": "cs", "id": "3", "text": "Večeři jsem si užil."}
  ]
}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()
pprint(languages)