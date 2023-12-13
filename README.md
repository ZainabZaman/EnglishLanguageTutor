# EnglishLanguageTutorWithLessonsEvaluation

## Lessons_Evaluation 

This project serves as an English Language Tutor, providing lessons and evaluating user responses for pronunciation, accuracy, completeness, fluency, and pitch.

## Overview

The English Language Tutor script incorporates multiple modules for assessing and tutoring users on different language-related aspects.

### Features

- Lessons on various topics.
- Pronunciation assessment.
- Fluency evaluation.
- Pitch analysis.

### Analysis
- Per lesson evaluation.
- Per lesson entry evaluation.
- Per word evaluation.
    
## Dependencies

Make sure to install the necessary dependencies through the provided requirements.txt file

```bash
pip install -r requirements.txt
```

Set your OpenAI API key. Replace YOUR_OPENAI_API_KEY in the code with your actual key.

### Usage
To use the application run the main file named as `lessons_evaluation.py` 
```python
python lessons_evaluation.py
```
The script includes predefined lessons in arrays for users to respond to. Customize the lessons based on your needs and the `option` variable lets the user decide which lessons he wants to work on. User responses are evaluated based on multiple criteria, including `accuacy`, `completeness`, `fluency`, `per_word_pitch`, `overall_pitch`, `relevancy`, providing an overall evaluation of each lesson based on these scores.
The script takes three inputs from the user
- Option: Lesson selection
- User text response: Textual response to the lesson entry
- User audio response: Speech response to the lesson entry

## Acknowledgments

- `Azure Speech SDK` is used for pronunciation evaluation 
 
