$location = "westeurope"
$rg_name = "CognitiveDemo" + (Get-Random -Minimum 10000 -Maximum 99999)
$cs_name = "CognitiveDemo" + (Get-Random -Minimum 10000 -Maximum 99999)

New-AzResourceGroup -Name $rg_name -Location $location

# https://docs.microsoft.com/en-us/powershell/module/az.cognitiveservices/new-azcognitiveservicesaccount?view=azps-4.8.0
# Check Type parameter 
#   https://docs.microsoft.com/en-us/powershell/module/az.cognitiveservices/get-azcognitiveservicesaccounttype?view=azps-4.8.0
#   AzCognitiveServicesAccountType
$cs = New-AzCognitiveServicesAccount -Name $cs_name -ResourceGroupName $rg_name -Location $location -SkuName S0 -Type CognitiveServices -Force

"Environment variables:"
"CV_RESOURCE_GROUP: " + $rg_name
"CV_ENDPOINT: " + $cs.Endpoint
"CV_LOCATION: " + $cs.Location

$keys = Get-AzCognitiveServicesAccountKey -Name $cs_name -ResourceGroupName $rg_name

"CV_KEY: " + $keys.Key1

# Put inforamation to temporary environment variable
# This information is lost after session is closed
$Env:CV_ENDPOINT = $cs.Endpoint
$Env:CV_KEY = $keys.Key1
$Env:CV_RESOURCE_GROUP = $rg_name
$Env:CV_LOCATION = $cs.Location