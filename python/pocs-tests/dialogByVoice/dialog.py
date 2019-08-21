import speech_recognition as sr
import pyttsx3
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

engine = pyttsx3.init()

engine.setProperty('rate', 200)
engine.setProperty('volume', 0.5)

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

r = sr.Recognizer()

#######################

bot = ChatBot('Jarvis')

greetings_assistant = ['Hi Jarvis', 'Hello sir', 'Hello Jarvis', 'Hi sir']

greetings_morning = ['Good morning Jarvis', 'Good morning sir']

greetings_afternoon = ['Good afternoon Jarvis', 'Good afternoon sir']

greetings_night = ['Good night Jarvis', 'Good night sir']

calling_assistant = ['Jarvis are you there', 'At your service sir', 'Jarvis are you awake', 'For you, always', 'Jarvis', 'Yes sir']

identification = ['Who are you', 'Iam Jarvis, a personal virtual assistant', 
'What are you', 'A personal virtual assistant']

purpose = ['Why do you exists', 'To help people in you domestic and professional tasks', 
'What is your purpose', 'To help people in you domestic and professional tasks']

# explain_purpose = []

trainer = ListTrainer(bot)

trainer.train(greetings_assistant)
trainer.train(greetings_morning)
trainer.train(greetings_afternoon)
trainer.train(greetings_night)
trainer.train(calling_assistant)
trainer.train(identification)
trainer.train(purpose)

with sr.Microphone() as source:
    while True:
        print('Say something: ')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print('You said: {}'.format(text))
            textToTalk = bot.get_response(text)
            print("Assistant ", textToTalk)
            engine.say(textToTalk)
            engine.runAndWait()
            engine.stop()
        except:
            print('Sorry')
