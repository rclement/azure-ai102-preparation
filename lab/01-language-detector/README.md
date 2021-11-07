# Azure AI-102 Certification Lab Exercise: Language Detector

> Let's discover Azure Cognitive Services by building a simple language detector!

Original inspiration:

- [Create and consume Cognitive Services Module](https://docs.microsoft.com/en-us/learn/modules/create-manage-cognitive-services/)
- [Lab Website](https://microsoftlearning.github.io/AI-102-AIEngineer/Instructions/01-get-started-cognitive-services.html)
- [Python Code on GitHub](https://github.com/MicrosoftLearning/AI-102-AIEngineer/tree/master/01-getting-started/Python)

## REST API Version

The first method to access Cognitive Services APIs is to use the REST API interface.

Documentation: [Cognitive Services API - Text Analytics - Languages](https://docs.microsoft.com/en-us/rest/api/cognitiveservices-textanalytics/3.0/languages/languages)

The Python source file [01-language-detector/language_detector_api.py](01-language-detector/language_detector_api.py)
provides a sample code interacting with this API.

### Goal

Complete the program by filling the blanks in the `detect_language` function.

### Expected usage

```bash
$ python 01-language-detector/language_detector_api.py
Enter text: hello mon nom est John
Detected language French with 60.0% confidence
```

## SDK Version

The second method to access Cognitive Services APIs is to use the official SDK.

Documentation: [Cognitive Services Python SDK - Text Analytics - Detect Language](https://docs.microsoft.com/en-us/python/api/azure-ai-textanalytics/azure.ai.textanalytics.textanalyticsclient?view=azure-python#detect-language-documents----kwargs-)

The Python source file [01-language-detector/language_detector_sdk.py](01-language-detector/language_detector_sdk.py)
provides a sample code interacting with this SDK.

### Goal

Complete the program by filling the blanks in the `detect_language` function.

### Expected usage

```bash
$ python 01-language-detector/language_detector_sdk.py
Enter text: hello mon nom est John
Detected language French with 60.0% confidence
```
