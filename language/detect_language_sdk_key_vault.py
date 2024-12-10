import os
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
from azure.keyvault.secrets import SecretClient
from azure.ai.textanalytics import TextAnalyticsClient

from dotenv import load_dotenv

load_dotenv()

endpoint = os.environ.get("CV_ENDPOINT")
keyvault_uri = os.environ.get("KEYVAULT_URI")

# Create a SecretClient object
client = SecretClient(vault_url=keyvault_uri, credential=DefaultAzureCredential())

# Retrieve the secret
service_key = client.get_secret("stbechyn-ai-multiservice-key")

text_analytics_client = TextAnalyticsClient(endpoint, AzureKeyCredential(service_key.value))

documents = [
    {"id": "1", "text": "This is a document written in English."},
    {"id": "2", "text": "Este es un document escrito en Español."},
    {"id": "3", "text": "这是一个用中文写的文件"},
    {"id": "4", "text": "Tento dokument je česky."}
]

response = text_analytics_client.detect_language(documents = documents)

for document in response:
    print("Document Id: ", document.id, ", Language: ", document.primary_language.name)