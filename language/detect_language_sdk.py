import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

from dotenv import load_dotenv

load_dotenv()

key = os.environ.get("CV_KEY")
endpoint = os.environ.get("CV_ENDPOINT")

text_analytics_client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

documents = [
    {"id": "1", "text": "This is a document written in English."},
    {"id": "2", "text": "Este es un document escrito en Español."},
    {"id": "3", "text": "这是一个用中文写的文件"},
    {"id": "4", "text": "Tento dokument je česky."}
]

response = text_analytics_client.detect_language(documents = documents)

for document in response:
    print("Document Id: ", document.id, ", Language: ", document.primary_language.name)