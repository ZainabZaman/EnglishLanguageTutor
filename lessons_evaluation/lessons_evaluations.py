#-------------- IMPORTING DEPENDENCIES -------------
import openai
import pronounce_assessment_file
import tts
import intonation
import get_audio 
import relevancy

#-------------- API KEYS -------------
openai.api_key = 'YOUR_OPENAI_API_KEY'
voice_name = 'en-US-JennyMultilingualNeural'

#-------------- AUDIO FILE TO SAVE USER AUDIO RESPONSE -------------
user_response_output = 'user_response_audio.wav'

#-------------- VARIABLES THAT DO NOT NEED TO BE CLEARED FOR EACH ITERATION -------------
combined_dict = {}
accuracy_result = 0
completeness_result = 0
fluency_result = 0
pitch_result = 0
lesson = 0
# relevancy_score = 'irrelevant'

#-------------- DEFINING LESSONS -------------
# lesson_01 = ['what is your favorite food and why?', 'what is your favorite color and why?', 'what is your hobby and why?']

lesson_01 = ['What\'s your favorite type of book?', 'How often do you read books?', 'How long does it take you to finish a book?', 'Where do you read books?', 'What\'s the most interesting book you have ever read?']
lesson_02 = ['What\'s your favorite tourist attraction?', 'Do you prefer traveling alone or joining a guided tour?', 'How many places have you traveled to?', 'What do you usually do during your trip?', 'Do you prefer traveling by car, train or plane?']
lesson_03 = ['How many people are there in your family?', 'Does your family live in a house or an apartment?', 'Do you have any siblings?', 'Does your family usually have dinner together?', 'Would you prefer to have a big family or a small family?']
lesson_04 = ['Do you like to cook?', 'Do you eat out or cook at home?', 'What\'s your favorite food?', 'What do you usually eat for breakfast?', 'Is there any kind of food you don\'t like?']
lesson_05 = ['What\'s the weather like in your country?', 'What kind of weather do you like?', 'Do you usually watch the weather forecast?', 'What\'s your favorite season?', 'Do you like it when it rains?']
lesson_06 = ['What is the most popular means of transport in your country?', 'How do you go to school or work?', 'Do you prefer public transport or private transport?', 'How often do you use public transport?', 'What is the most environmentally friendly form of transportation?']
lesson_07 = ['Do you usually exercise?', 'What sport do you play?', 'How often do you exercise?', 'Where do you exercise?', 'What benefits can you get from exercising?']
lesson_08 = ['What\'re your favorite means of communication?', 'Do you usually write letters or emails?', 'Do you use social networks?', 'How to you keep in touch with your friends and family?', 'Do you have good communication skills in your opinion?']
lesson_09 = ['What sport do you like?', 'Is it easy to play that sport?', 'How long have you been practicing that sport?', 'Do you like watching sports online or offline?', 'Why is sport important?']
lesson_10 = ['do you like going to parties?', 'What do you usually wear when you come to a party?', 'Do people have to bring anything to the party?', 'Do you prefer big or small parties?', 'Do you like playing party games?']



#-------------- LANGUAGE TUTORING FUNCTION -------------
def tutor():
    global accuracy_result, completeness_result, fluency_result, pitch_result
    option = input('Enter lesson number [1-10]: ')
    option = int(option)
    if option == 1: 
        lesson = lesson_01
    elif lesson == 2:
        lesson = lesson_02
    elif lesson == 3:
        lesson = lesson_03
    elif lesson == 4:
        lesson = lesson_04
    elif lesson == 5:
        lesson = lesson_05
    elif lesson == 6:
        lesson = lesson_06
    elif lesson == 7:
        lesson = lesson_07
    elif lesson == 8:
        lesson = lesson_08
    elif lesson == 9:
        lesson = lesson_09
    elif lesson == 10:
        lesson = lesson_10

    #-------------- ITERATING THROUGH EACH ENTRY IN A LESSON ARRAY -------------
    for i in range(len(lesson)):
        #-------------- DEFINED INSIDE LOOP COZ WE NEED THEM CLEARED FOR EACH ITERATION -------------
        results_combined = []
        accuracy = ''
        completeness = ''
        fluency = ''
        per_word_evaluation = ''
        pitch_per_word = ''
        overall_pitch = ''
        user_response = ''
        relevancy_score = 0.0

        #-------------- GETTING ENTRIES FROM LESSON ARRAY -------------
        print('Tutor: ', lesson[i])
        tts.text_to_speech(tts.voice_name, lesson[i])

        #-------------- GETTING USER TEXT RESPONSE -------------
        user_response = input('User: ')
        relevancy_score = relevancy.relevant(lesson[i], user_response)
        while relevancy_score < 0.65: 
            print('Provide a more relevant response!')
            user_response = input('User: ')
            relevancy_score = relevancy.relevant(lesson[i], user_response)
        if relevancy_score > 0.6:
            user_response_words = user_response.split(' ')
            tts.text_to_speech(tts.voice_name, user_response)

            #-------------- GETTING USER AUDIO RESPONSE -------------
            get_audio.get_audio(user_response_output)

            #-------------- GETTING EVALUATION SCORES -------------
            accuracy, completeness, fluency, per_word_evaluation = pronounce_assessment_file.pronunciation_assessment_continuous_from_file(user_response_output, 'en-US', user_response)
            # print(pronounciation_assessment)
            pitch_per_word, overall_pitch = intonation.pitch(user_response_words, user_response_output)

            #-------------- APPENDING PER ITERATION RESULTS INTO COMBINED RESULTS DICTIONARY -------------
            results_combined.append(f'accuracy: {accuracy}, completeness: {completeness}, fluency: {fluency}, per word evaluaiton: {per_word_evaluation}, per word pitch: {pitch_per_word}, overall pitch: {overall_pitch}')
            combined_dict[lesson[i]] = (results_combined)
            # for word in pronounciation_assessment:
            #     accuracy = word.accuracy_score
            #     # print(accuracy)

            #-------------- GETTING OVERALL EVALUATION SCORES FOR ONE COMPLETE LESSON -------------
            accuracy_result = accuracy_result + accuracy
            completeness_result = completeness_result + completeness
            fluency_result = fluency_result + fluency
            pitch_result = pitch_result + overall_pitch
            # print('Combined Dictionary: ', combined_dict)
    accuracy_result = accuracy_result/len(lesson)
    completeness_result = completeness_result/len(lesson)
    fluency_result = fluency_result/len(lesson)
    pitch_result = pitch_result/len(lesson)

    #-------------- PRINTING OVERALL AND PER RESPONSE EVALUATION RESULTS -------------
    print(f'     Evaluation of lesson-01: Accuracy:{accuracy_result}, Completeness: {completeness_result}, Fluency: {fluency_result}, Pitch: {pitch_result}')
    print('     Replies Evaluation: ', combined_dict)

tutor()

