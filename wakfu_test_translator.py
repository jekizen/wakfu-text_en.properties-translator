from typing import List

import deep_translator.exceptions
import requests
import os
import PySimpleGUI as sg
import time
import re

from deep_translator import GoogleTranslator as googtr

gtr = googtr(source='auto', target='ru')



# Get the username of the current user
username = os.getlogin()

# Wakfu chat log file path
chat_log_file = f'texts_en.properties'
file2 = f'translated.txt'
fileerr = f'errors.txt'

# Google Translate API endpoint
translate_api_endpoint = 'https://translate.googleapis.com/translate_a/single'
#translate_api_endpoint = 'https://translate.googleapis.com/language/translate/v2'

# Default translation settings
from_lang = 'auto'
to_lang = 'ru'

# GUI setup
sg.theme("DarkTeal9")  # Set the window theme to a dark theme

layout = [[sg.Multiline(size=(180, 20), key="-OUTPUT-", auto_refresh=True, autoscroll=False)],
          [sg.Text("Count lines in translated file"), sg.In(size=(100, 1), enable_events=True, key="-count2-")],
          [sg.Text("     Count lines in target file"), sg.In(size=(100, 1), enable_events=True, key="-counttarget-")],
          [sg.Text("                       Progress:"), sg.In(size=(100, 1), enable_events=True, key="-progress-")],
          [sg.Multiline(size=(180, 10), key="-INFO1-", auto_refresh=True, autoscroll=False)],
          [sg.ProgressBar(1000, orientation='h', size=(51, 10), key='progressbar')]
          ]
window = sg.Window("Wakfu texts_en.properties Translator", layout, finalize=True)


def translate_message(message):
    # Build the translation API query
    query_params = {
        'client': 'gtx',
        'sl': from_lang,
        'tl': to_lang,
        'model': 'nmt',
        'backend': 10,
        'dt': 't',
        'q': message,
    }
    response = requests.get(translate_api_endpoint, params=query_params)

    # Extract the translated text from the response
    data = response.json()
    translated_text = data[0][0][0]

    return translated_text


def update_chat_log():
#    i = 1

    count2 = 0



    #if os.stat(file2).st_size == 0:
    try:
        with open(file2, 'r', encoding='utf-8') as temp:
            for count2, line in enumerate(temp):
                window["-count2-"].update(str(count2))
                window.refresh()
                # window["-INFO1-"].update('Count lines in translated file:'+ str(count2), append=False)
    #else:
    except FileNotFoundError:
        with open(file2, 'w', encoding='utf-8') as temp:
            temp.write('')
            count2 = 0
            window["-count2-"].update(str(count2))
            window.refresh()


    num_lines = count2 + 1
    with open(chat_log_file, 'r', encoding='utf-8') as f:
        for num_lines, line in enumerate(f):
            # num_lines = 100
            window["-counttarget-"].update(str(num_lines))
            window.refresh()
            # window["-INFO1-"].update('Count lines in target file:'+str(num_lines) + '\n', append=True)

    #thererun=count2
    with open(chat_log_file, 'r', encoding='utf-8') as f:
        line: str
        countLine: int
        # ii: int
        for countLine, line in enumerate(f):
            if countLine<=count2:
                continue
            # translated_message =line.rstrip()
            s = line.splitlines()[-1]
            # s=line.rstrip()

            s2 = s.split('=', 1)
            try:
                s3 = gtr.translate(text=s2[1])
            except Exception as err:
                s3 = s2[1]
                window["-INFO1-"].update(str(err) + '\n', append=True)
                window["-INFO1-"].update("Check to string:" + '\n', append=True)
                window["-INFO1-"].update(s2[0] + '=' + s2[1] + '\n\n', append=True)
                with open(fileerr, 'a+', encoding='utf-8') as ffeerr:
                    ffeerr.write(str(err) + '\n' + s2[0] + '=' + s2[1] + '\n\n')
                pass

            if s3 == None:
                 s3 = s2[1]
                 window["-INFO1-"].update("Error, string = None"+ '\n', append=True)
                 window["-INFO1-"].update("Check to string:"+ '\n', append=True)
                 window["-INFO1-"].update(s2[0]+'=' + s2[1] + '\n\n', append=True)
                 with open(fileerr, 'a+', encoding='utf-8') as ffeerr:
                     ffeerr.write("Check to string:"+ '\n'+s2[0]+'=' + s2[1] + '\n\n')
                 #pass

            if countLine % 200 == 0:
                window["-OUTPUT-"].update(' ' + '\n', append=False)
            translated_message = s2[0] + '=' + s3
            window["-OUTPUT-"].update('en: '+s2[1] + '\n\n', append=True)
            window["-OUTPUT-"].update('ru: '+s3 + '\n\n\n', append=True)

            window["-progress-"].update(str(countLine) + ': all =' + str(num_lines))
            window['progressbar'].UpdateBar(int(countLine * 1000 / num_lines))
            # window.refresh()

            time.sleep(0.01)
            with open(file2, 'a', encoding='utf-8') as temp:
                temp.write(translated_message + '\n')

        # with open("temp.txt", 'w') as fw:
        # time.sleep(100)
        # latest_message = chat_log.splitlines()[i]
        # translated_message = translate_message(latest_message)
        # window["-OUTPUT-"].update(translated_message + '\n', append=True)
        # i=i+1

    # Extract the latest chat message
    # latest_message = chat_log.splitlines()[-1]
    # latest_message = chat_log.splitlines()[i]
    # i=i+1

    # Translate the latest message
    # translated_message = translate_message(latest_message)

    # Display the translated message in the GUI window
    # window["-OUTPUT-"].update(translated_message + '\n', append=True)

    # return i


def monitor_chat_log():
    last_mtime = os.stat(chat_log_file).st_mtime
    while True:
        time.sleep(1)
        mtime = os.stat(chat_log_file).st_mtime
        if mtime != last_mtime:
            last_mtime = mtime
            update_chat_log()


# Start monitoring the chat log file in a separate thread
# import threading
# monitor_thread = threading.Thread(target=monitor_chat_log, daemon=True)
# monitor_thread.start()

# Start updating the chat log
update_chat_log()

# Start the GUI event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()
