import pyaudio
import wave

# output_wav_file = "user_audio.wav"

def get_audio(output_wav_file):


    # Specify the output WAV file
    output_wav_file = output_wav_file

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Set audio parameters
    format = pyaudio.paInt16
    channels = 1
    rate = 16000  # Adjust the sample rate as needed
    chunk = 1024  # The size of each audio chunk
    record_seconds = 5  # The duration for recording

    # Create a PyAudio stream to capture audio
    stream = audio.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)

    print("Recording...")

    audio_frames = []

    for i in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        audio_frames.append(data)

    print("Recording finished.")

    # Save the recorded audio to a WAV file
    with wave.open(output_wav_file, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(audio_frames))

    # print(f"Recorded audio saved to {output_wav_file}")

    # Cleanup
    stream.stop_stream()
    stream.close()
    audio.terminate()
