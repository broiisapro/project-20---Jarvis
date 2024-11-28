import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import wikipedia
import os
import webbrowser
import time

# Initialize the recognizer and the speaker
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak to the user
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
        except sr.UnknownValueError:
            speak("Sorry, I could not understand what you said. Please try again.")
            command = listen()
        except sr.RequestError:
            speak("Sorry, there seems to be a problem with the speech service.")
            command = listen()
        return command

# Function for checking the time
def tell_time():
    now = datetime.datetime.now()
    speak(f"The time is {now.strftime('%H:%M:%S')}")

# Function for telling a joke
def tell_joke():
    speak("Why don't skeletons fight each other? They don't have the guts.")

# Function for opening applications or websites
def open_website(command):
    if "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif "new document" in command:
        webbrowser.open("https://www.docs.new")
    elif "documents" in command:
        webbrowser.open("https://docs.google.com/document/u/0/")
    elif "new slide" in command:
        webbrowser.open("https://www.slides.new")
    elif "slides" in command:
        webbrowser.open("https://docs.google.com/presentation/u/0/")
    elif "new spreadsheet" in command:
        webbrowser.open("https://www.sheets.new")
    elif "spreadsheet" in command:
        webbrowser.open("https://docs.google.com/spreadsheets/u/0/")
    
    else:
        speak("Sorry, I cannot open that website.")

# Main function to handle different commands
def execute_command(command):
    command = command.lower()

    if "hello" in command or "hi" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        tell_time()
    elif "joke" in command:
        tell_joke()
    elif "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song}")
        kit.playonyt(song)
    elif "search" in command:
        query = command.replace("search", "").strip()
        speak(f"Searching for {query}")
        kit.search(query)
    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "").strip()
        try:
            result = wikipedia.summary(topic, sentences=1)
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("There are multiple results, please be more specific.")
        except wikipedia.exceptions.HTTPTimeoutError:
            speak("I could not fetch the Wikipedia page, please check your connection.")
    elif "open" in command:
        open_website(command)
    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("Sorry, I did not understand that command.")

# Main loop to keep the assistant listening
def main():
    speak("Hello, I am your assistant. How can I help you?")
    while True:
        command = listen()
        execute_command(command)

if __name__ == "__main__":
    main()
