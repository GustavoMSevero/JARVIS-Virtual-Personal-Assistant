#import module pyttsx3
import pyttsx3

#initialization
engine = pyttsx3.init()

#set properties if you want
engine.setProperty('rate', 200)
engine.setProperty('volume', 0.5)

# getting details of current speaking rate
#rate = engine.getProperty('rate')

#getting details of current voice
voices = engine.getProperty('voices')
#id of the voice i chose
engine.setProperty('voice', voices[0].id)

text = "Hi! I am Jarvis, a personal virtual assistant"

engine.say(text)
engine.runAndWait()
engine.stop()