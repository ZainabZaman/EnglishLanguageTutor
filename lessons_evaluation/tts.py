import azure.cognitiveservices.speech as speechsdk
import threading 
import wave 
import time

weatherfilename = 'output.wav'
pronunciation_assessment_config = speechsdk.PronunciationAssessmentConfig(json_string="{\"referenceText\":\"good morning\",\"gradingSystem\":\"HundredMark\",\"granularity\":\"Phoneme\",\"EnableMiscue\":true}")
speech_key = "YOUR_AZURE_APEECH_STUDIO_KEY"
service_region = "eastus"

output_filename = 'output_audio.wav'
voice_name = 'en-US-JennyMultilingualNeural'
input_text = "Hi, this is Jenny Multilingual. How are you!"

def text_to_speech(voice_name, input_text):

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # Note: the voice setting will not overwrite the voice element in input SSML.
    speech_config.speech_synthesis_voice_name = voice_name

    text = input_text

    # use the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    result = speech_synthesizer.speak_text_async(text).get()

    if result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

# text_to_speech(voice_name, input_text)

def text_to_speech_wav(voice_name, input_text, output_filename):

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # Note: the voice setting will not overwrite the voice element in input SSML.
    speech_config.speech_synthesis_voice_name = voice_name

    text = input_text

    # use the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    result = speech_synthesizer.speak_text_async(text).get()

    # Check result
    audio_data = result.audio_data
    with open(output_filename, "wb") as wav_file:
        wav_file.write(audio_data)
    print(f"Audio saved to {output_filename}")

    if result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

# text_to_speech_wav(voice_name, input_text, output_filename)