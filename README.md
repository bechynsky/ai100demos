# AI-10X demos
Demos for [AI-10X](https://docs.microsoft.com/en-us/learn/certifications/exams/ai-100) training and certification. It can be used by trainer or by attendees as homework.

# Before you start
- Become familiar with [Azure Cloud Shell](https://docs.microsoft.com/en-us/azure/cloud-shell/overview).
- Become familiar with [Az.CognitiveServices](https://docs.microsoft.com/en-us/powershell/module/az.cognitiveservices/?view=azps-5.0.0#cognitive-services) PowerShell module.
- Become familiar with [Environment Variables](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7).

# How to use

- Login to [Azure Cloud Shell](https://shell.azure.com).
- Clone this repository.
  - ```git clone https://github.com/bechynsky/ai100demos.git```
- Install Python libraries.
- Run [new_cognitiveservices.ps1](new_cognitiveservices.ps1).
  - All information like endpoint and service key is stored in Environment variables. 
  - It is not persistent and information is lost after Azure Cloud Shell restarts.
  - Copy output of script for future reference.
