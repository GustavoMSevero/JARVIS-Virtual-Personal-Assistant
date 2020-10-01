from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Jarvis')

# greetings = ['Hi', 'Hello', 'Hello', 'Hi', 'Hey', 'Oh, hi', 'Oh, hi', 'hey, hello']

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

while True:
    question = input("You ")
    answer = bot.get_response(question)
    print("Assistant ", answer)
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!") 

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('okay')

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('okay')

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak('okay')

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak('okay')
