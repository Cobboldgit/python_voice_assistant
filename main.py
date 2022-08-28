from datetime import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        print('Playing ' + song)
        kit.playonyt(song)
    elif 'time' in command:
        time = datetime.now().strftime("%I:%M %p")
        print(time)
        talk('The time is ' + time)
    elif 'who is' in command:
        try:
            talk('Searching Wikipedia')
            command_data = command.replace('who is ', '')
            info = wikipedia.summary(command_data, sentences=4)
            print(info)
            talk(info)
        except Exception as error:
            print(error)
    elif 'joke' in command:
        talk('ok. I will make you laugh ')
        talk(pyjokes.get_joke())
    else:
        talk('Sorry!, come again')


while True:
    run_alexa()
