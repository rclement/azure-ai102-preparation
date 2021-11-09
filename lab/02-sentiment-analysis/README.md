# Azure AI-102 Certification Lab Exercise: Sentiment Analysis

> Let's discover the Azure Cognitive Service Text Analytics by building a sentiment analyzer!

Original inspiration:

- [Lab Website](https://microsoftlearning.github.io/AI-102-AIEngineer/Instructions/05-analyze-text.html)
- [Python Code on GitHub](https://github.com/MicrosoftLearning/AI-102-AIEngineer/tree/master/05-analyze-text/Python)

## Sentiment Analysis

To perform sentiment analysis over arbitrary text, you will need to first detect
the language then analyze the sentiment given the text and its detected language.

Documentation:

- [Cognitive Services Python SDK - Text Analytics - Detect Language](https://docs.microsoft.com/en-us/python/api/azure-ai-textanalytics/azure.ai.textanalytics.textanalyticsclient?view=azure-python#detect-language-documents----kwargs-)
- [Cognitive Services Python SDK - Text Analytics - Analyze Sentimenbt](https://docs.microsoft.com/en-us/python/api/azure-ai-textanalytics/azure.ai.textanalytics.textanalyticsclient?view=azure-python#analyze-sentiment-documents----kwargs-)

### Goal

Complete the notebook [sentiment_analysis.ipynb](sentiment_analysis.ipynb).

### Expected usage

```bash
$ python 02-sentiment-analysis/sentiment_analysis_solution.py
Text to analyze: J'ai adoré ce film, malgré un début chaotique
Detected French text with positive sentiment
(90.0% positive, 0.0% neutral, 10.0% negative)
```
