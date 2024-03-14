
from clipboardActions import paste_value
from xtts import speak

def process_llm_response(text):
  if "JUST_SAY" in text:
    # Extract text after "JUST_SAY" for speaking
    start_index = text.find("JUST_SAY") + len("JUST_SAY") + 1
    speak_text = text[start_index:].strip()
    speak(speak_text) 
  elif "CODE_COPY_PASTE" in text or "CODE_START" in text:
    # Extract code between "CODE_START" and "CODE_END" for pasting
    start_index = text.find("CODE_START") + len("CODE_START") + 1
    end_index = text.find("CODE_END")
    code_snippet = text[start_index:end_index].strip()
    paste_value(code_snippet)
  else:
    # TODO add some more actions 
    print(f"Unrecognized instruction: {text}") 


# llm_response = "JUST_SAY I'm Jarvis"
# process_llm_response(llm_response)
