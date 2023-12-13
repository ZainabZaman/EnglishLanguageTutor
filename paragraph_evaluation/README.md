# English Language Tutor Reading Paragraph Evaluation

## Overview

This project integrates advanced language tutoring features, including pronunciation assessment, fluency evaluation, and pitch analysis. The script incorporates various modules for language assessment and tutoring.

## Dependencies

Ensure you have the necessary dependencies installed by running the following command:

```bash
pip install -r requirements.txt
```
Replace YOUR_OPENAI_API_KEY in the code with your actual OpenAI API key and 'YOUR_AZURE_SPEECH_STUDIO_API_KEY' with your azure speech studio key.

## Modules
- openai: Integration with OpenAI API.
- pronounce_assessment_file: Module for pronunciation assessment.
- tts: Text-to-speech functionality.
- intonation: Module for pitch analysis.
- relevancy: Assessing relevancy of user responses.
- stt: Speech-to-text functionality.
- azure.cognitiveservices.speech: Azure Speech SDK for pronunciation evaluation.
- grammar_vocabulary_evaluation: Module for grammar and vocabulary evaluation.

## Usage
The script narrates a paragraph for the user and then takes a narration input of the same paragraph from the user and evaluates responses based on various criteria, including accuracy, completeness, fluency, prosody scores, per-word evaluation, pitch per word, overall pitch, and relevancy score.
To use the application, execute the main file, `readung_paragraph_evaluation.py`:
```python
python readung_paragraph_evaluation.py
```
## Acknowledgments
This project utilizes the Azure Speech SDK for robust pronunciation evaluation.

