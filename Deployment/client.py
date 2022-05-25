import speech_recognition as sr
import requests
import json
import time



while True:

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)

    # recognize speech using Google Speech Recognition
        message = recognizer.recognize_google(audio)
        print(message)

    response = requests.post(f'http://127.0.0.1:8000/predict?message={message}')
    response

    time.sleep(10)


