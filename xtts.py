import pyttsx3

def speak(text, rate=150):
  engine = pyttsx3.init()
  engine.setProperty('rate', rate)
  engine.say(text)
  engine.runAndWait()

# text_to_speak = "Hellow, Jarvis here."
# speak(text_to_speak)
