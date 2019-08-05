#import module pyttsx3
import pyttsx3

#initialization
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('volume', 0.5)
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)
for voice in voices:
    print("Voices")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)