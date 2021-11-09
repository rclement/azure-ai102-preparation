# Azure AI-102 Certification Lab Exercises

Here are a series of lab exercises to discover and get a hands-on
Azure Cognitive Services in order to prepare to take Azure AI-102 certification.

These exercises are greatly inspired by Microsoft Learning content for the AI-102 Lab:

- [Website](https://microsoftlearning.github.io/AI-102-AIEngineer/)
- [GitHub](https://github.com/MicrosoftLearning/AI-102-AIEngineer)

## Requirements

- Python 3.8
- (optional) Pipenv
- (optional) Conda

## Setup

### Python

Install the following Python packages into a virtual environment:

- `azure-ai-textanalytics`
- `azure-cognitiveservices-vision-computervision`
- `jupyter`
- `matplotlib`
- `pillow`
- `python-dotenv`
- `requests`

If you are using Pipenv you can simply run `pipenv install` in this directory.

### Azure

In order to use Azure Cognitive Services APIs, you need to create an Azure
Cognitive Services resource on your Azure Portal:

1. Go to the Azure portal: https://portal.azure.com
2. Click on "Create a resource" button
3. Search for "Cognitive Services" and create a "Cognitive Services" resource with the following settings:
    - Subscription: your Azure subscription
    - Resource group: choose or create a resource group
    - Region: choose your preferred region
    - Name: enter a unique name for your resource
    - Pricing tier: "Standard S0"
3. (Alternative) For free Cognitive Services resources, create specific resources such as "Text Analytics" with the "Free F0" pricing tier selected
4. Select the required checkboxes and click on "Review and Create"
5. Wait for deployment to complete, then click on "View Resource"
6. Go to the "Keys and Endpoint" page and take note of the following:
    - "Endpoint": the HTTP endpoint to which client applications can send requests
    - "KEY 1" / "KEY 2": two keys that can be used for authentication (use either key to authenticate)
    - "Location/Region": the location where the resource is hosted (required for requests to some APIs)
7. Copy the `.example.env` file to `.env`
8. Update the `.env` file:
    - `COG_SERVICE_ENDPOINT`: replace the value with the "Endpoint" value from your Cognitive Serices resource
    - `COG_SERVICE_KEY`: replace the value with either the "KEY 1" or "KEY 2" value from your Cognitive Services resource
