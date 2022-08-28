import json
from sys import modules
from urllib.request import urlopen


def news(speak):
    try:
        jsonObj: urlopen("")
        data = json.load(jsonObj)
        i = 1

        speak('Here are some top news')

        for item in data['articles']:
            print(str(i) + '. ' + item['title'] + '\n')
            print(item['de'] + '\n')
            speak(str(i) + '. ' + item['title'] + '\n')
            i += 1

    except Exception as e:
        print(e)
        speak('Sorry, It seems you have low internet connectivity')


modules[__name__] = news
