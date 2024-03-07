# WARNING - doesn't work in Azure Cloud Shell. Run it on local computer.

import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

load_dotenv()

subscription_key = os.environ.get("CV_KEY")
service_region = os.environ.get("CV_LOCATION")


speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=service_region)

# Replace with the languages of your choice, from list found here: https://aka.ms/speech/tts-languages
speech_config.speech_synthesis_voice_name = "cs-CZ-VlastaNeural"

# Creates a speech synthesizer using the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# Receives a text from console input.
print("Type some text that you want to speak...")
text = input()

# Synthesizes the received text to speech.
# The synthesized speech is expected to be heard on the speaker with this line executed.
result = speech_synthesizer.speak_text_async(text).get()

# Checks result.
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized to speaker for text [{}]".format(text))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
    print("Did you update the subscription info?")