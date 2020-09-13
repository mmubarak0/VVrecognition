import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

# save the voice that have been generated from text
def speak(text):
    # gtts define expected word that will be converted from audio file
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    # then playsound simulate the response with human voice
    playsound.playsound(filename)

# get the voice input from the user
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

# handel input 
text = get_audio()
if "hello" in text:
    speak("hi how are you")
if "i am fine" in text:
    speak("that is good")
