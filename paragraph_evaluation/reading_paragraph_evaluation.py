#-------------- IMPORTING DEPENDENCIES -------------
import openai
import pronounce_assessment_file
import tts
import intonation
import relevancy
import stt
import azure.cognitiveservices.speech as speechsdk
import grammar_vocabulary_evaluation


#-------------- API KEYS -------------
openai.api_key = 'YOUR_OPENAI_API_KEY'
voice_name = 'en-US-JennyMultilingualNeural'

#-------------- AUDIO FILE TO SAVE USER AUDIO RESPONSE -------------
# user_response_output = 'user_response_audio.wav'
filename = 'F:\GPT\language_tutor\speechaudiofiles\im good how are you (1).wav'
combined_dict = {}

def iteration_evaluation(lesson_entry, filename):
    results_combined = []
    accuracy = ''
    completeness = ''
    fluency = ''
    per_word_evaluation = ''
    pitch_per_word = ''
    overall_pitch = ''
    prosody_scores = ''
    user_response = ''
    relevancy_score = 0.0

    #-------------- GETTING ENTRIES FROM LESSON ARRAY -------------
    print('Tutor: ', lesson_entry)
    tts.text_to_speech(tts.voice_name, lesson_entry)

    #-------------- GETTING USER TEXT RESPONSE -------------
    user_response_audio = filename
    user_response = stt.recognize_from_microphone(user_response_audio)
    relevancy_score = relevancy.relevant(lesson_entry, user_response)
    print('Relevancy Score: ', relevancy_score)
    if relevancy_score < 0.65:
        print('Provide a more relevant response!')

    if relevancy_score > 0.65:
        user_response_words = user_response.split(' ')
        tts.text_to_speech(tts.voice_name, user_response)

        #-------------- GETTING EVALUATION SCORES -------------
        accuracy, completeness, fluency, per_word_evaluation, prosody_scores = pronounce_assessment_file.pronunciation_assessment_continuous_from_file(user_response_audio, 'en-US', user_response)
        # print(pronounciation_assessment)
        pitch_per_word, overall_pitch = intonation.pitch(user_response_words, user_response_audio)

        #-------------- APPENDING PER ITERATION RESULTS INTO COMBINED RESULTS DICTIONARY -------------
        results_combined.append(f'accuracy: {accuracy}, completeness: {completeness}, fluency: {fluency}, prosody score: {prosody_scores}, per word evaluaiton: {per_word_evaluation}, per word pitch: {pitch_per_word}, overall pitch: {overall_pitch}')
        combined_dict[lesson_entry] = (results_combined)
        # print(combined_dict)

        # return combined_dict
        print(f'Accuracy: {accuracy, type(accuracy)} \nCompleteness: {completeness, type(completeness)} \nFluency: {fluency, type(fluency)} \nProsody score: {prosody_scores} \nPer Word Evaluation: {per_word_evaluation, type(per_word_evaluation)} \nPitch Per Word: {pitch_per_word, type(pitch_per_word)} \nOverall Pitch: {overall_pitch, type(overall_pitch)} \nRelevancy Score: {relevancy_score, type(relevancy_score)}')

        #-------------- RETURNING accuracy, completeness, fluency, per_word_evaluation, pitch_per_word, overall_pitch, relevancy_score  -------------
        return accuracy, completeness, fluency, per_word_evaluation, pitch_per_word, overall_pitch, relevancy_score, prosody_scores

iteration_evaluation('Cars have played a pivotal role in shaping the modern world. These four-wheeled marvels of engineering have revolutionized transportation, providing individuals with unprecedented mobility and convenience. From the early days of the Ford Model T to the electric and autonomous vehicles of the future, cars have continuously evolved, offering improved safety features, efficiency, and cutting-edge technology. They have become more than just a mode of transportation; they are a symbol of freedom, status, and personal expression. Whether you\'re cruising down an open highway, navigating through busy city streets, or embarking on a cross-country road trip, cars are a fundamental part of our daily lives, offering both practicality and a sense of adventure. As the automotive industry continues to innovate, we can anticipate even more exciting developments that will shape the future of transportation.', filename)
