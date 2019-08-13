from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Jarvis')

greetings = ['Hi', 'Hello', 'Hello', 'Hi', 'Hey', 'Oh, hi', 'Oh, hi', 'hey, hello']

identification = ['Who are you', 'Iam Jarvis, a personal virtual assistant', 
'What are you', 'A personal virtual assistant']

trainer = ListTrainer(bot)
trainer.train(greetings)
trainer.train(identification)

while True:
    question = input("Você ")
    anwser = bot.get_response(question)
    print("bot ", anwser)