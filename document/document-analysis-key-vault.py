import os
from dotenv import load_dotenv

from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


load_dotenv()
keyvault_uri = os.environ.get("KEYVAULT_URI")
endpoint = os.getenv("ENDPOINT")


# Create a SecretClient object to access the secret in the key vault
client = SecretClient(vault_url=keyvault_uri, credential=DefaultAzureCredential())

# Retrieve the secret
key = client.get_secret("stbechyn-document").value


# Store connection information

credential=AzureKeyCredential(key)

fileUri = "https://github.com/MicrosoftLearning/mslearn-ai-document-intelligence/blob/main/Labfiles/01-prebuild-models/sample-invoice/sample-invoice.pdf?raw=true"
fileLocale = "en-US"
fileModelId = "prebuilt-invoice"

print(f"\nConnecting to Forms Recognizer at: {endpoint}")
print(f"Analyzing invoice at: {fileUri}")

# Create the client
document_analysis_client = DocumentAnalysisClient(
     endpoint=endpoint, credential=credential
)

# Analyse the invoice
poller = document_analysis_client.begin_analyze_document_from_url(
     fileModelId, fileUri, locale=fileLocale
)


# Display invoice information to the user
receipts = poller.result()
    
for idx, receipt in enumerate(receipts.documents):    
    vendor_name = receipt.fields.get("VendorName")
    if vendor_name:
        print(f"\nVendor Name: {vendor_name.value}, with confidence {vendor_name.confidence}.")

    customer_name = receipt.fields.get("CustomerName")
    if customer_name:
        print(f"Customer Name: '{customer_name.value}, with confidence {customer_name.confidence}.")


    invoice_total = receipt.fields.get("InvoiceTotal")
    if invoice_total:
        print(f"Invoice Total: '{invoice_total.value.symbol}{invoice_total.value.amount}, with confidence {invoice_total.confidence}.")

print("\nAnalysis complete.\n")