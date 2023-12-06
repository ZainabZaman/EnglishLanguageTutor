import parselmouth
import numpy as np
import tts

# per_word_pitch = []
# input_sentence = 'We will start from the basics and then move onto the complex phrases'
# input_words = input_sentence.split(' ')
# print(type(input_sentence))
# output = 'output_file.wav'
# tts.text_to_speech_wav(tts.voice_name, input_sentence, output)

def pitch(input_words, output):
    per_word_pitch = []
    # input_words = input_sentence.split(' ')
# Load the recorded audio using parselmouth
    sound = parselmouth.Sound(output)

    # Calculate pitch
    pitch = sound.to_pitch()
    # print(pitch)

    # Extract pitch values
    pitch_values = pitch.selected_array['frequency']
    pitch = [x for x in pitch_values if x != 0]
    for i in range(len(input_words)):
        # print(f"{input_words[i]} = Pitch: {pitch[i]:.2f}")
        per_word_pitch.append(f'{input_words[i]}: {pitch[i]} Hz')
    # print(per_word_pitch)
    # Calculate the overall average pitch
    overall_average_pitch = np.mean(pitch)

    # Print the overall average pitch value
    # print(f"Overall Pitch: {overall_average_pitch:.2f} Hz")

    return per_word_pitch, overall_average_pitch
