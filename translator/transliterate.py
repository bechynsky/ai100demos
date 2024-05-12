import os

from azure.ai.translation.text import *
from azure.ai.translation.text.models import InputTextItem

from dotenv import load_dotenv

load_dotenv()

key = os.environ.get("KEY")
endpoint = os.environ.get("ENDPOINT")
location = os.environ.get("LOCATION")

content = [InputTextItem(text="こんにちは")]

credential = TranslatorCredential(key, location)

client = TextTranslationClient(endpoint=endpoint, credential=credential)
result = client.transliterate(content=content, language="ja", from_script="Jpan", to_script="Latn")
print(result)

