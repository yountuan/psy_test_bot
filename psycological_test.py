import telebot
from telebot import types
from decouple import config

token = config('TOKEN')
bot = telebot.TeleBot(token=token)
name = ""
step = 1
answers = {}

@bot.message_handler(commands=['start'])
def start_test(message):
    bot.send_message(message.from_user.id, "Hello. Enter your name, please.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global name, step
    global answers
    if not name:
        name = message.text
        bot.send_message(message.from_user.id, f"Welcome to the psychological test, {name}!\nDon't think. \nAnswer the first thing that comes to mind.\nTell about your feelings.")
        bot.send_message(message.from_user.id, "Let's start. \nType 'ok' to begin and 'q' to quit.")
    elif message.text.lower() == 'ok' and step == 1:
        answers["1"] = message.text
        bot.send_message(message.from_user.id, "You stand on the shore and look into the distance.🌅 \nWhat do you feel?")    
        step =2
    elif step ==2:
        answers["2"] = message.text
        bot.send_message(message.from_user.id, "You are walking in a forest and look down at your feet.🌲🪵🌿 \nWrite down your feelings.")
        step = 3
    elif step ==3:
        answers["3"] = message.text
        bot.send_message(message.from_user.id, "You watch the flight of seagulls. \nHow did you feel? ")
        step = 4
    elif step ==4:
        answers["4"] = message.text
        bot.send_message(message.from_user.id, "You met a herd of horses. 🐎🐎🐎\nWhat do you feel?")
        step = 5
    elif step ==5:
        answers["5"] = message.text
        bot.send_message(message.from_user.id, "You are walking through the desert and a wall appears in front of you. There is a small hole in it behind which there is an oasis.🏝️ \nWhat will you do? ")
        step = 6
    elif step ==6:
        answers["6"] = message.text
        bot.send_message(message.from_user.id, "You are very thirsty and suddenly you see a jug of water.💧🏺 \nWill you drink without hesitation?")
        step = 7
    elif step ==7:
        answers["7"] = message.text
        bot.send_message(message.from_user.id, "You are lost in the forest. It was already dark - and suddenly you saw a house with a light on. 🛖🕯️\nYour actions.")
        step = 8
    elif step ==8:
        answers["8"] = message.text
        bot.send_message(message.from_user.id, "Imagine that you are in a heavy fog. 🌁😶‍🌫️\nWhat will you do?")
        step =9
    elif step ==9:
        bot.send_message(message.from_user.id, "We have finished the test. \nNow let's go to see the results. \nType 'go' to see results. ")
        step=10
    elif step ==10 and message.text.lower() == 'go':
        show_results(message)
    elif message.text.lower() == 'q':
        bot.send_message(message.from_user.id, "You quitted successfully.")
    else:
        bot.send_message(message.from_user.id, "Invalid value. Only 'ok' or 'q'.")

    return


@bot.message_handler(func=lambda message: message.text.lower() == 'go')
def trigger_show_results(message):
    show_results(message)

def show_results(message):
    bot.send_message(message.from_user.id, f"{name}, your responses:")
    for key, value in answers.items():
        if key == "1":
            bot.send_message(message.from_user.id, f"1. Your answer for the question about shore and looking at distance 🌅: \n\n{value} - this is your attitude to life, emotions and feelings.")
        elif key == "2":
            bot.send_message(message.from_user.id, f"2. Your answer for the question about forest 🌲🪵🌿: \n\n{value} - this is how you feel in your origin family.")
        elif key == "3":
            bot.send_message(message.from_user.id, f"3. Your answer for the question about seagulls: \n\n{value} - this is your attitude towards women.")
        elif key == "4":
            bot.send_message(message.from_user.id, f"4. Your answer for the question about herd of horses 🐎🐎🐎: \n\n{value}  - this is your attitude towards men.")
        elif key == "5":
            bot.send_message(message.from_user.id, f"5. Your answer for the question about dessert and oasis inside the hole 🏝️: \n\n{value} - this is your main life strategy, goal. How you solve your problems.")
        elif key == "6":
            bot.send_message(message.from_user.id, f"6. Your answer for the question about jug of water 💧🏺: \n\n{value} - this is your your selectivity. Choosing your partner.")
        elif key == "7":
            bot.send_message(message.from_user.id, f"7. Your answer for the question about light inside a house in the forest 🛖🕯️: \n\n{value} - this is your readiness for marriage.")
        elif key == "8":
            bot.send_message(message.from_user.id, f"8. Your answer for the question about heavy fog 🌁😶‍🌫️: \n\n{value} - this is your attitude towards death.")
    return

bot.polling(none_stop=True, interval=0, timeout=35)

