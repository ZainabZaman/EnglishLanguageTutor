# English Language Tutor With Lessons Evaluation

## Project Overview

The **English Language Tutor With Lessons Evaluation** project is designed to serve as an advanced English language tutor, offering lessons on various topics and providing comprehensive evaluations of user responses, including pronunciation, accuracy, completeness, fluency, and pitch.

### Key Features

- **Lesson Modules:** Engage in lessons covering a wide range of topics.
- **Pronunciation Assessment:** Evaluate pronunciation accuracy for improved language skills.
- **Fluency Evaluation:** Assess user responses for fluency and coherence.
- **Pitch Analysis:** Analyze speech pitch for enhanced communication skills.

### Detailed Analysis

The project includes a thorough analysis at various levels:

- **Per Lesson Evaluation:** Obtain an overall evaluation for each lesson.
- **Per Lesson Entry Evaluation:** Assess user responses for individual lesson entries.
- **Per Word Evaluation:** Evaluate pronunciation and fluency at the word level.

## Dependencies

Ensure you have the required dependencies installed by running the following command:

```bash
pip install -r requirements.txt
```
Replace YOUR_OPENAI_API_KEY in the code with your unique API key.

## Usage
To utilize the application, execute the main file, `lessons_evaluation.p`y:
```python
python lessons_evaluation.py
```
The script incorporates predefined lessons in arrays for users to respond to. The option variable allows users to select specific lessons. User responses are meticulously evaluated based on criteria such as accuracy, completeness, fluency, per-word pitch, overall pitch, and relevancy. This comprehensive evaluation provides valuable feedback on each lesson.

The script prompts users for three inputs:

- Option: Choose a lesson for focused learning.
- User Text Response: Provide a textual response to the lesson entry.
- User Audio Response: Deliver a speech response to the lesson entry.

## Acknowledgments
This project acknowledges the use of the Azure Speech SDK for robust pronunciation evaluation.
