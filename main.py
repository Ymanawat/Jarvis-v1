import time
import keyboard
import speech_recognition as sr
from analyzeLLMOutput import process_llm_response
from clipboardActions import copy_from_active_window, paste_value
from geminiScript import generate_text
from utils import log
from xtts import speak

# Global variable to store the last log time
recognizer_is_running = False

def get_speech_input():
    """Listens for continuous speech and returns sentences."""
    log("Listening for speech...")
    recognizer = sr.Recognizer()
    print(recognizer)
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1  # pause time
        audio_data = recognizer.listen(source)
        # print(audio_data)

        try:            
            # Split transcript using punctuation for sentence endings
            delimiters = ".?!"
            sentences = recognizer.recognize_google(audio_data).split(delimiters)
            print(sentences)

            # Remove empty strings
            sentences = [s for s in sentences if s]
            return sentences
        except sr.UnknownValueError:
            print("unkwon value error")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")
            return None 

def start_recognition():
    """Starts continuous speech recognition with sentence detection."""
    global recognizer_is_running
    recognizer_is_running = True
    print(recognizer_is_running)
    while recognizer_is_running:
        sentences = get_speech_input()
        text_from_window = copy_from_active_window()
        if sentences:
            for sentence in sentences:
                # processing text sending to LLM
                processed_value = generate_text(sentence + "\n" + text_from_window) 
                if (processed_value == None):
                    speak('Some error occured while processing your query, please try again')
                else :
                    process_llm_response(processed_value)
        time.sleep(0.5)

    print('not running')

def stop_recognition():
    """Stops the continuous recognition loop."""
    global recognizer_is_running
    recognizer_is_running = False

def on_hotkey_press():
    global recognizer_is_running
    if recognizer_is_running:
        log("Hotkey pressed, stopping recognition")
        stop_recognition()
    else:
        log("Hotkey pressed, starting recognition")
        start_recognition()

# Register hotkeys for recognition start/stop
keyboard.add_hotkey('f8', on_hotkey_press)
keyboard.add_hotkey('esc', stop_recognition)

# Keep the script running to listen for hotkey presses
while True:
    time.sleep(1)

