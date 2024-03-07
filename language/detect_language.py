import os
import requests

# pprint is used to format the JSON response
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

subscription_key = os.environ.get("CV_KEY")
endpoint = os.environ.get("CV_ENDPOINT")


language_api_url = endpoint + "text/analytics/v3.0/languages"

documents = {"documents": [
    {"id": "1", "text": "This is a document written in English."},
    {"id": "2", "text": "Este es un document escrito en Español."},
    {"id": "3", "text": "这是一个用中文写的文件"},
    {"id": "4", "text": "Tento dokument je česky."}
]}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()
pprint(languages)