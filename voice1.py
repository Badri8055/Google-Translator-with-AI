
import speech_recognition as sr
from google_trans_new import google_translator
import pyttsx3
recognizer =sr.Recognizer()
engine=pyttsx3.init()

with sr.Microphone() as source:
    print("clearing the backgroundnoise")
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("waiting for message")
    audio=recognizer.listen(source,timeout=1) 
    print("Done Recording")

try:
    print("recognizing")
    result=recognizer.recognize_google(audio,language='en')
except Exception as ex:
    print(ex)

#translation function
def trans():
    langinput=input("enter language to translate")
    translator=google_translator()
    translator_text=translator.translate(str(result),lang_tgt=str(langinput))
    print(translator_text)
    engine.say(str(translator_text))
    engine.runAndWait()
trans()