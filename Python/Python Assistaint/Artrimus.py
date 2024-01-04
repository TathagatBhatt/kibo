import smtplib
import os
import webbrowser
import wikipedia
import pyttsx3
import speech_recognition as sr
import datetime
import random as r
import subprocess

print("Initializing Artrimus")
engine = pyttsx3.init('sapi5')
vocies = engine.getProperty("voices")
engine.setProperty('voice',vocies[1].id)
# Allows Artrimus to Talk
def speak(text):
    engine.say(text)
    engine.runAndWait()
speak("Initializing Artrimus...")

# Artrimus Wishes Me
def wishMe():
    L = ["Greetings","Hello","Welcome Back", "Welcome","Hey There"]
    speak(r.choice(L)+"Kibo")
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Aftertoon")
    else :
        speak("Good Evening")
    speak('I am Artrimus , How may i help you ?')   
wishMe()

# take command from user via a microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        audio = r.listen(source)
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said {query}\n")
    except Exception as e :
        speak("Say That Again Please")
        query = None
    return query
query = takeCommand()

# execute tasks as per user query
spotify_path = ''
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
if 'wikipedia' in query.lower():
    speak('Searching wikipedia')
    query = query.replace('wikipedia','')
    results = wikipedia.summary(query,sentences = 4)
    speak(results)
elif 'youtube' in query.lower():
    speak("opening Youtube...")
    url = 'youtube.com'
    webbrowser.get(chrome_path).open(url)
    webbrowser.get(chrome_path).open(url)
elif 'spotify' in query.lower():
    speak("opening Spotify...")
    os.system('start spotify://')