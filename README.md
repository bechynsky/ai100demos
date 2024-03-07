# AI-10X demos
Demos for [AI-10X](https://docs.microsoft.com/en-us/learn/certifications/exams/ai-100) training and certification. It can be used by a trainer or by attendees as homework. The goal is to understand how to call and use REST API for Cognitive Services.

# Before you start
- Become familiar with [Azure Cloud Shell](https://docs.microsoft.com/en-us/azure/cloud-shell/overview).
- Become familiar with [Az.CognitiveServices](https://docs.microsoft.com/en-us/powershell/module/az.cognitiveservices/?view=azps-5.0.0#cognitive-services) PowerShell module.
- Become familiar with [Environment Variables](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7).
- Become familiar with [Cognitive Services REST API](https://westeurope.dev.cognitive.microsoft.com/docs/services).
- Read comments in code.

## Where to put endpoint and key

Service endpoint and key you need to add to [environment variable](https://en.wikipedia.org/wiki/Environment_variable). Another option is to create [_.env_ file](https://pypi.org/project/python-dotenv/) and add it to this file. Example of _.env_ file:

```
CV_ENDPOINT="https://xxxxxxxxxxxxx.cognitiveservices.azure.com/"
CV_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
CV_LOCATION="xxxxxxxx"
```

## Speech

Demos using speech needs audio files. Some sample audio files are included. Information about [supported audio format](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/rest-speech-to-text#audio-formats).

### How to create audio samples

- Record audio sample using Windows 10 Voice Recorder. It produces _.m4a_ audio file.
- Search for _.m4a to .wav converter online_.
- Convert _.m4a_ to _.wav_ file using an online tool.
- Rename file to _message-[LANGUAGE_CODE](https://aka.ms/speech/tts-languages).wav_. For example ```message-cs-CZ.wav```.
- Copy audio file to [speech_translator/](speech_translator/) folder.

### Limitation
Python code using a microphone and a speaker doesn't work in Azure Cloud Shell. You need to run that locally. All Azure Cloud Shell unsupported demos are in the [speech_translator/local_pc_folder](speech_translator/local_pc_only/) folder. 


# How to use

- Login to [Azure Cloud Shell](https://shell.azure.com).
- Clone this repository.
  - ```git clone https://github.com/bechynsky/ai100demos.git```
- Install Python libraries.
  - ```pip install azure-cognitiveservices-speech```
- Goto ```ai100demos``` folder.
- Run ```code .``` to open VS Code to see the code.
- Run [new_cognitiveservices.ps1](new_cognitiveservices.ps1).
  - All information like endpoint and service key is stored in Environment variables. 
  - Check environment variables we create ```printenv | grep CV_``` or ```Get-ChildItem env:* | Where-Object {$_.Name -like 'CV_*'}```.
  - It is not persistent and information is lost after Azure Cloud Shell restarts.
  - Copy output of the script for future reference.

# Cognitive Services REST API playground
If you want to change calls to REST API you can test it first.

- Open [API Testing Console](https://westeurope.dev.cognitive.microsoft.com/docs/services)
- Use search on the top right to find an API.
- Choose the API you are looking for.
- Choose a method you want to test on the left (1) and then click your region (2).
- Now you can create a REST API Call and test it.

![REST API Test Console](rest_api_test_1.jpg)


# Cleanup
- Run ```cleanup.ps1``` to delete resources in Azure
- Delete the ```ai100demos``` folder 
