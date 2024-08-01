import os

from azure.ai.translation.text import *
from azure.ai.translation.text.models import InputTextItem
from azure.core.credentials import AzureKeyCredential

from dotenv import load_dotenv

load_dotenv()

key = os.environ.get("KEY")
endpoint = os.environ.get("ENDPOINT")
location = os.environ.get("LOCATION")

content = ["こんにちは"]

credential = AzureKeyCredential(key)

client = TextTranslationClient(region=location, credential=credential)


result = client.transliterate(body=content, language="ja", from_script="Jpan", to_script="Latn")
print(result)

