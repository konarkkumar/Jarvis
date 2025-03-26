import speech_recognition as sr
import webbrowser
import pyttsx3
import musicliberary
from openai import OpenAI
from gtts import gTTS 
import pygame
import os

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")

    # Initialize the mixer module
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")

    # Play the music
    pygame.mixer.music.play()

    print("Playing... Press CTRL+C to stop.")

    # Keep the program running while the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        
    pygame.mixer.music.unload()
    os.remove("temp.mp3")
    
def aiProcess(command):
    client = OpenAI(api_key="Use your Api Key",
    )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return(completion.choices[0].message.content)

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://www.twitter.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicliberary.music[song]
        webbrowser.open(link)
        
    else:
        #Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)
        

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        #Listen for the wake word "Jarvis"
        # obtaib audio from the microphone
        r = sr.Recognizer()
        
        #recognize speech using Google
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout= 5, phrase_time_limit= 3)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya, I am listening")
                #Listen for the command
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source)
                command = r.recognize_google(audio)
                processCommand(command)
                
        except Exception as e:
            print("Error; {0}".format(e))
