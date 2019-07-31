import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        print('Say something: ')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print('You said: {}'.format(text))
        except:
            print('Sorry')