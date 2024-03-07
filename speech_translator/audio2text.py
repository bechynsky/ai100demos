import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

load_dotenv()

subscription_key = os.environ.get("CV_KEY")
service_region = os.environ.get("CV_LOCATION")

speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=service_region)

# Creates a speech recognizer using a file as audio input, also specify the speech language
# Replace with the languages of your choice, from list found here: https://aka.ms/speech/tts-languages
# It is case sensitive
LANGUAGE_CODE = 'cs-CZ'

# audio file patern 'message-LANGUAGE_CODE.wav'
audio_file = "message-{0}.wav".format(LANGUAGE_CODE)
audio_config = speechsdk.audio.AudioConfig(filename=audio_file)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language=LANGUAGE_CODE, audio_config=audio_config)


# Starts speech recognition, and returns after a single utterance is recognized. The end of a
# single utterance is determined by listening for silence at the end or until a maximum of 15
# seconds of audio is processed. It returns the recognition text as result.
# Note: Since recognize_once() returns only a single utterance, it is suitable only for single
# shot recognition like command or query.
result = speech_recognizer.recognize_once()

# Check the result
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
