import speech_recognition as sr
import pyttsx3
from pywhatkit import playonyt
import datetime
import wikipedia
import pyjokes
import pyaudio
import pdb
import smtplib
import pywhatkit


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def engine_talk(text):
    engine.say(text)
    engine.runAndWait()


def run_ana():
    # command taking input
    command = take_command()
    print(command)

    if(command is not None):
        if 'play' in command:
            song = command.replace('play', '')
            engine_talk('Playing' + song)
            pywhatkit.playonyt(song)
        # if 'play' in command:
        #     # cur.execute("select link from command where word='play'")
        #     # d=cure.fetchall()
        #     song = command.replace(d)
        #     talk('playing ' + song)
        #     playonyt(song)

        # tells you the current time
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
            print("Current time is ", time)

        elif 'mail' in command:
            print("what would you want to say")
            talk("what would you want to say")
            with sr.Microphone() as au:
                maudio = listener.listen(au)
                mess = listener.recognize_google(maudio)
                print(mess)
            receiver = command.replace('send a mail to', '')
            # print(receiver)
            password = "vxmpclucstkjvbtj"
            send = "dtry2023@gmail.com"
            res = {' Ram': 'dhruvchhalani26@gmail.com',
                   ' Dhruv': 'dhruvchhalani@gmail.com'}
            # print(res[receiver])
            r = res[receiver]
            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()
            server.login(send, password)
            server.sendmail(send, r, mess)
            server.quit()
            print("Mail succesfully sent")
            engine_talk("Mail succesfully sent")

        elif 'ana stop' in command:
            exit(0)

        elif 'anastop' in command:
            exit(0)

        # gives you information
        elif 'give me info about' in command:
            print('here it goes.')
            talk('here it goes.')
            person = command.replace('give me info about', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)

        elif 'friends' in command:
            print("I am your best friend.")
            talk("I am your best friend.")
            talk("when I am here, you don't have to worry about anything.")
            print("when I am here, you don't have to worry about anything.")

        elif 'Hello'.lower() in command:
            print('Hello! I am Ana, nice to meet you')
            talk('Hello! I am Ana, nice to meet you')

        elif 'day' in command:
            day = datetime.datetime.now().strftime("%A")
            print("Today is ", day)
            talk("Today is " + day)

        # tells you a joke
        elif 'joke'.lower() in command:
            talk('here is a joke for you.')
            print('here is a joke for you.')
            talk(pyjokes.get_joke())
            a = pyjokes.get_joke()
            print(a)

        # introducing itself
        elif 'yourself'.lower() in command:
            talk("Hello! I am Ana here.")
            talk("I am your customisable personal assistant.")
            print("Hello! I am Ana here.")
            print("I am your customisable personal assistant.")

    else:
        talk('Please say the command again.')
        print('Please say the command again.')


# wishes the user in the beginning
def wishclock():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        print("Good Morning!")
        talk("Good Morning!")
        print("Have a great day ahead.")
        talk("Have a great day ahead.")

    elif hour >= 12 and hour < 18:
        print("Good Afternoon.")
        talk("Good Afternoon.")

    else:
        print("Good evening")
        talk("Good evening")
        print("reminding you to journal about your day.")
        talk("reminding you to journal about your day.")
wishclock()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # begins speaking by introducing itself
        print("This is your assistant Ana speaking.")
        talk("This is your assistant Ana speaking.")
        print("Please tell me how may i help you?")
        talk("Please tell me how may i help you?")
        r.energy_threshold = 7000

        # Starts Listening
        audio = r.listen(source)
        print("Thanks!")
        talk("Thanks!")
        print("Fetching the results.")
        talk("Fetching the results.")

    try:
        # Recognizes audio in English
        text = r.recognize_google(audio)
        command = text
        return command

    except:
        # When there is no notable speech
        print("Sorry, couldn't hear you!")
        talk("Sorry, couldn't hear you!")
        print("The command was not clear to me.")
        talk("The command was not clear to me.")
        pass


while True:
    run_ana()
