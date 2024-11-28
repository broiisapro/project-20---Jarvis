# Voice Assistant Python Project

This is a simple voice assistant application built with Python that can respond to voice commands and perform a variety of tasks such as telling the time, telling jokes, searching the web, playing music, and more. The assistant uses speech recognition for input, text-to-speech for output, and integrates with several Python libraries to provide functionality.

## Features

- **Speech Recognition**: The assistant listens to the user's voice commands and processes them using Google's speech recognition API.
- **Text-to-Speech**: The assistant responds using text-to-speech to provide feedback and responses.
- **Web Browsing**: The assistant can open websites like YouTube, Google, Facebook, and Google Docs.
- **Search and Play**: It can search the web or play a song on YouTube using `pywhatkit`.
- **Wikipedia Integration**: It can fetch summaries from Wikipedia for a given topic.
- **Time & Jokes**: The assistant can tell the current time and tell jokes.

## How It Works

### 1. **Listening to Commands**
   The assistant listens to your voice through the microphone using the `speech_recognition` library. It captures the audio and converts it to text using Google's speech-to-text API.

### 2. **Executing Commands**
   Based on the recognized text, the assistant can:
   - **Tell the time**: Responds with the current time.
   - **Tell a joke**: Tells a random joke.
   - **Play music**: Searches and plays a song on YouTube using `pywhatkit`.
   - **Search**: Searches the web for a query using `pywhatkit`.
   - **Open websites**: Opens websites like Google, Facebook, or Google Docs in your default web browser.
   - **Wikipedia Search**: Fetches a short summary from Wikipedia on a given topic.
   - **Exit**: Exits the program when the user says "exit" or "quit".

### 3. **Text-to-Speech**
   After processing the command, the assistant uses the `pyttsx3` library to respond to the user with text-to-speech.

### 4. **Error Handling**
   If the assistant does not understand the command or encounters an error, it will prompt the user to try again. It also handles possible errors like disambiguation issues with Wikipedia or problems with the speech recognition service.

## Project Structure

- `recognizer`: Handles speech recognition.
- `engine`: Initializes text-to-speech engine.
- `listen()`: Listens for a voice command.
- `speak(text)`: Converts text to speech.
- `tell_time()`: Tells the current time.
- `tell_joke()`: Tells a joke.
- `open_website(command)`: Opens specific websites based on user commands.
- `execute_command(command)`: Processes commands and executes the corresponding functions.
- `main()`: Runs the assistant in an infinite loop, listening for commands.

## Example Commands

- **"hello"** or **"hi"**: Greets the user.
- **"time"**: Tells the current time.
- **"joke"**: Tells a joke.
- **"play music"**: Plays a song on YouTube (e.g., "play Shape of You").
- **"search"**: Searches Google for a topic (e.g., "search Python programming").
- **"wikipedia"**: Retrieves a Wikipedia summary of a topic (e.g., "wikipedia Python").
- **"open YouTube"**: Opens YouTube in a browser.
- **"exit"** or **"quit"**: Exits the program.
