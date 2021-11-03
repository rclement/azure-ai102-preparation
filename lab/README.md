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
4. Select the required checkboxes and click on "Review and Create"
5. Wait for deployment to complete, then click on "View Resource"
6. Go to the "Keys and Endpoint" page and take note of:
    - Endpoint: the HTTP endpoint to which client applications can send requests
    - KEY 1 / KEY 2: two keys that can be used for authentication (use either key to authenticate)
    - Location: the location where the resource is hosted (required for requests to some APIs)
7. Copy the `.example.env` file to `.env`
8. Update the `.env` file:
    - `COG_SERVICE_ENDPOINT`: replace the value with the "Endpoint" value from your Cognitive Serices resource
    - `COG_SERVICE_KEY`: replace the value with either the "KEY 1" or "KEY 2" value from your Cognitive Services resource

## 01 - Language Detector

Let's discover Azure Cognitive Services by building a simple language detector!

Original inspiration:

- [Lab Website](https://microsoftlearning.github.io/AI-102-AIEngineer/Instructions/01-get-started-cognitive-services.html)
- [Python Code on GitHub](https://github.com/MicrosoftLearning/AI-102-AIEngineer/tree/master/01-getting-started/Python)

### REST API Version

The first method to access Cognitive Services APIs is to use the REST API interface.

Documentation: [Cognitive Services API - Text Analytics - Languages](https://docs.microsoft.com/en-us/rest/api/cognitiveservices-textanalytics/3.0/languages/languages)

The Python source file [01-language-detector/language_detector_api.py](01-language-detector/language_detector_api.py)
provides a sample code interacting with this API.

**Goal: complete the program by filling the blanks in the `detect_language` function.**

**Expected usage**:

```bash
$ python 01-language-detector/language_detector_api.py
Enter text: hello mon nom est John
Detected language French with 60.0% confidence
```

### SDK Version

The second method to access Cognitive Services APIs is to use the official SDK.

Documentation: [Cognitive Services Python SDK - Text Analytics - Detect Language](https://docs.microsoft.com/en-us/python/api/azure-ai-textanalytics/azure.ai.textanalytics.textanalyticsclient?view=azure-python#detect-language-documents----kwargs-)

The Python source file [01-language-detector/language_detector_sdk.py](01-language-detector/language_detector_sdk.py)
provides a sample code interacting with this SDK.

**Goal: complete the program by filling the blanks in the `detect_language` function.**

**Expected usage**:

```bash
$ python 01-language-detector/language_detector_sdk.py
Enter text: hello mon nom est John
Detected language French with 60.0% confidence
```
