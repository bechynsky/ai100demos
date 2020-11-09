$location = "westeurope"
$rg_name = "CognitiveDemo" + (Get-Random -Minimum 10000 -Maximum 99999)
$cs_name = "CognitiveDemo" + (Get-Random -Minimum 10000 -Maximum 99999)

New-AzResourceGroup -Name $rg_name -Location $location

# https://docs.microsoft.com/en-us/powershell/module/az.cognitiveservices/new-azcognitiveservicesaccount?view=azps-4.8.0
# Check Type parameter 
#   https://docs.microsoft.com/en-us/powershell/module/az.cognitiveservices/get-azcognitiveservicesaccounttype?view=azps-4.8.0
#   AzCognitiveServicesAccountType
$cs = New-AzCognitiveServicesAccount -Name $cs_name -ResourceGroupName $rg_name -Location $location -SkuName S0 -Type CognitiveServices -Force

$keys = Get-AzCognitiveServicesAccountKey -Name $cs_name -ResourceGroupName $rg_name

# Put inforamation to temporary environment variable
# This information is lost after session is closed
$Env:CV_ENDPOINT = $cs.Endpoint
$Env:CV_KEY = $keys.Key1
$Env:CV_RESOURCE_GROUP = $rg_name
$Env:CV_LOCATION = $cs.Location

# Print demo related environment variables
Get-ChildItem env:* | Where-Object {$_.Name -like 'CV_*'} | Select-Object -Property Name, Value | Format-Table