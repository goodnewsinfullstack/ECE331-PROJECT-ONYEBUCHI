import speech_recognition as sr
import time


def transcribe_audio_file(filename):
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(filename)

    with audio_file as source:
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.record(source)

    try:
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"Transcription: {query}")
    except sr.RequestError as error:
        print(f"Failed to transcribe the audio. Error: {error}")
    except sr.UnknownValueError:
        print("Unable to recognize the speech in the audio.")


if __name__ == "__main__":
    transcribe_audio_file("Goodnews POD.wav")
    time.sleep(10)
    print("Quitting the program now")
