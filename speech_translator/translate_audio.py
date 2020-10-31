# WARNING - doesn't work in Azure Cloud Shell. Run it on local computer.

import os
import azure.cognitiveservices.speech as speechsdk

subscription_key = os.environ.get("CV_KEY")
service_region = os.environ.get("CV_LOCATION")

# Creates an instance of a speech translation config with specified subscription key and service region.
# Replace with your own subscription key and region identifier from here: https://aka.ms/speech/sdkregion
translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=subscription_key, region=service_region)

# Sets source and target languages.
# Replace with the languages of your choice, from list found here: https://aka.ms/speech/sttt-languages
LANGUAGE_CODE = 'cs-CZ'
toLanguage = 'en'
translation_config.speech_recognition_language = LANGUAGE_CODE
translation_config.add_target_language(toLanguage)

# audio file patern 'message-LANGUAGE_CODE.wav'
audio_file = "message-{0}.wav".format(LANGUAGE_CODE)
audio_config = speechsdk.audio.AudioConfig(filename=audio_file)

# Creates a translation recognizer using and audio file as input.
recognizer = speechsdk.translation.TranslationRecognizer(translation_config=translation_config, audio_config=audio_config)
result = recognizer.recognize_once()

# Check the result
if result.reason == speechsdk.ResultReason.TranslatedSpeech:
    print("RECOGNIZED '{}': {}".format(LANGUAGE_CODE, result.text))
    print("TRANSLATED into {}: {}".format(toLanguage, result.translations[toLanguage]))
elif result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("RECOGNIZED: {} (text could not be translated)".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("NOMATCH: Speech could not be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    print("CANCELED: Reason={}".format(result.cancellation_details.reason))
    if result.cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("CANCELED: ErrorDetails={}".format(result.cancellation_details.error_details))
