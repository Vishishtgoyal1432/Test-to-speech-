# # project 1: 
# name : Text to Speech 
#  by: vishisht goyal 
# 1 install gtts  (googel text to speech)
# 2 install speechRecognition 
# 3 install pyaudio
# install playsound
import gtts
import speech_recognition as voice

import playsound

from gtts import gTTS

import os

audio_string = ''' FUCK YOU '''
tts = gTTS(text=audio_string , lang="en")

audio_file = "audio.mp3"
tts.save(audio_file)
playsound.playsound(audio_file)


os.remove(audio_file) #if you want to save the mp3 file in local folder remove this line .....


# ---------------------------------------#

# import pyttsx3

# engine   =  pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# print(voices[0].id)
# engine.setProperty('voices' , voices[0].id) 

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
