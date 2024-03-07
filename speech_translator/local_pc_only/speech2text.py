# WARNING - doesn't work in Azure Cloud Shell. Run it on local computer.

import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

load_dotenv()

subscription_key = os.environ.get("CV_KEY")
service_region = os.environ.get("CV_LOCATION")



speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=service_region)

# Replace with the languages of your choice, from list found here: https://aka.ms/speech/tts-languages
# speech_config.speech_recognition_language="en-US"
speech_config.speech_recognition_language="cs-CZ"

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

result = speech_recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))