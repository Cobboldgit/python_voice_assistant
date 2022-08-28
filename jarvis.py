import subprocess
import wolframalpha
import pyttsx3
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
# import feedparser
import smtplib
import ctypes
import time
import shutil
# from twilio.rest import Client
# from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import pywhatkit as kit

# custome modules
import calculator
import news


# ==== Engine ==== #
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# ==== program paths === #
programPath = {
    'vlc': 'C:/Program Files/VideoLAN/VLC/vlc.exe',
    'chrome': 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    'idm': 'C:/Program Files (x86)/Internet Download Manager/IDMan.exe',
    'mic': 'C:/Program Files (x86)/WOMic/WOMicClient.exe',
    'disk d': 'D:/',
    'music': 'C:/Users/augus/Music'
}


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning Mister Cobbold!')
        speak('How are you doing today')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon Sir Cobbold!')
    else:
        speak('Good Evening Sir !')

    assname = ('Javis 1 point o')
    # speak('I am your Assistant')
    # speak(assname)
    # speak('I\'m ready for commands sir')


# def username():
#     speak('what should i call you sir')
#     uname = takeCommand()
#     speak('Welcome Mister ' + uname)
#     columns = shutil.get_terminal_size().columns

#     print('#####################'.center(columns))
#     print('Welcome Mr.', uname.center(columns))
#     print('#####################'.center(columns))

#     speak('How can i help you sir')


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception as error:
        print(error)
        print('Unable to Recognize your voice.')
        return 'None'

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


def main():
    if __name__ == '__main__':
        def clear(): return os.system('cls')

        clear()
        wishMe()
        # username()

    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query or 'who is' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace('wikipedia', "")
                query = query.replace('who is', "")
                results = wikipedia.summary(query, sentences=3)
                speak('According to wikipedia')
                print(results)
                speak(results)
            except Exception as e:
                speak('Sorry sir, something went wrong')
                print(e)

        # ==== open website ====
        elif 'open youtube' in query:
            speak('Here you go Youtube\n')
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            speak('Here you go Google\n')
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            speak('Here you go stack over flow. Happy coding\n')
            webbrowser.open('stackoverflow.com')

        # ==== search engine ==== #
        # elif 'search' in query:
        #     query = query.replace('search', '')
        #     webbrowser.open(query)
            

        # ==== open directories ====#
        elif 'play' in query:
            # speak('Here you go with music\n')
            # # music_dir = 'G:\\song'
            # songs = os.listdir(programPath['music'])
            # print(songs)
            # random = os.startfile(os.path.join(programPath['music'], songs[1]))
            song = query.replace('play', '')
            speak('playing ' + song)
            print('Playing ' + song)
            kit.playonyt(song)

        # ==== open apps ==== #
        elif 'vlc' in query:
            os.startfile(programPath['vlc'])

        # ==== system ==== #
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%I:%M p')
            speak(f'Sir, the time is {strTime}')

        elif 'lock window' in query:
            speak('locking the device')
            ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in query:
            speak('Ok sir ! see you later')
            speak('Your system will shut down in')
            i = 5
            for r in range(1, 6):
                speak(str(i))
                i -= 1
            subprocess.call('shutdown / p /f')

        elif 'restart' in query:
            speak('Ok sir')
            i = 5
            for r in range(1, 6):
                speak(str(i))
                i -= 1
            subprocess.call(['shutdown', '/r'])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif 'change background' in query:
            ctypes.windll.user32.SystemParameterInfow(
                20, 0, 'Location of wallpaper', 0)
            speak('Background changed successfully')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak('Recycle Bin Recycled')

        # ==== communition ==== #
        # elif 'email to gaurav' in query:
        #     try:
        #         speak('What should I say?')
        #         content = takeCommand()
        #         to = 'Reciever email address'
        #         sendEmail(to, content)
        #     except Exception as error:
        #         print(error)
        #         speak('I am not able to send this email')
        elif 'send a mail' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                speak('whome should I say')
                to = input()
                sendEmail(to, content)
                speak('Email has been sent !')
            except Exception as error:
                print(error)
                speak('I am not able to send this email')

        # ==== conversation ==== #
        elif 'how are you' in query:
            speak('I am fine, Thank you')
            speak('How are you, Sir')

        elif 'fine' in query or 'good' in query:
            speak("It's good to know that you are fine")
            speak('What can i do for you sir !')

        elif 'joke' in query:
            speak('Ok i will make you laugh')
            speak(pyjokes.get_joke())

        # ==== Javirs settings ==== #
        elif 'change my name to' in query:
            query = query.replace('change my name to', "")
            assname = query

        elif 'change name' in query:
            speak('What would you like to call me, Sir ')
            assname = takeCommand()
            speak('Thanks fro naming me')

        # ==== about Javirs ==== #
        elif "what is you name" in query or "what's your name" in query:
            speak('My friends call me')
            speak(assname)
            print('My friends call me', assname)

        # ==== utilities ==== #
        elif 'calculate' in query:
            answer = calculator(query)
            print('The answer is ' + answer)
            speak('The answer is ' + answer)

        # ==== find info ==== #
        elif 'news' in query:
            news(speak)

        elif 'where is' in query:
            query = query.replace('where is', '')
            subject = query
            speak('Give me a moment')
            webbrowser.open(
                'https://www.google.nl / maps/ place/' + subject + "")

        elif 'weather' in query:
            speak('My weather system is current not avaliable.')

        # ==== exit ==== #
        elif 'exit' in query:
            speak('Thanks for giving me your time')
            exit()


while True:
    main()
