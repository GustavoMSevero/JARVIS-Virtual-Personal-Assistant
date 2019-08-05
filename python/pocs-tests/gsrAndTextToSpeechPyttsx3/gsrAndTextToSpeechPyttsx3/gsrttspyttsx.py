import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 200)
engine.setProperty('volume', 0.5)

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

r = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        print('Say something: ')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print('You said: {}'.format(text))
            textToTalk = text
            engine.say(textToTalk)
            engine.runAndWait()
            engine.stop()
        except:
            print('Sorry')


