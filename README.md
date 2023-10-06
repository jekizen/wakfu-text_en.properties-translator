# wakfu-text_en.properties-translator
# 

This script is a Wakfu text_en.properties (from ~/.config/Ankama/zaap-steam/wakfu/contents/i18n/i18_en.jar) translator that reads text_en.properties file of the Wakfu game and translates in to file translated.txt using the Google Translate API. It provides a graphical user interface (GUI) where the translated messages are displayed.

Использован исходный текст из https://github.com/A-Charvin/WakfuChatTranslate и переделан для перевода большого файла text_en.properties.
Если работа программы прервалась, при новом пуске программа сканирует файл translated.txt, определяет количество переведенных ранее строк, и продолжает перевод с номера последней переведенной строки.


Used source text from https://github.com/A-Charvin/WakfuChatTranslate and modified it to translate a large text_en.properties file.
If the program is interrupted, when it is started again, the program scans the translated.txt file, determines the number of previously translated lines, and continues translation from the number of the last translated line.

for 


## Features

- Reads the latest chat messages from the Wakfu chat log file
- Translates the messages using the Google Translate API
- Supports automatic language detection and translation to English
- Updates the GUI with the translated messages in real-time
- Provides a simple and intuitive user interface

## Prerequisites

Before running the script, make sure you have the following installed:

- Python (version 3.6 or higher)
- Required Python libraries: requests, os, tkinter, PySimpleGUI

## Usage

1. Clone the repository or download the script file to your local machine.
2. Install the required Python libraries using pip: `pip install requests os tkinter PySimpleGUI`
3. Open a terminal or command prompt and navigate to the directory where the script is located.
4. Run the script using the command: `python wakfu_chat_translator.py`
5. The GUI window will open, displaying the translated messages as they are updated in the Wakfu chat log file.
6. Press `Alt + F12` to exit the program.

## Customization

You can customize the translation settings by modifying the following variables in the script:

- `from_lang`: The source language of the messages (default: auto)
- `to_lang`: The target language for translation (default: en)

## License

This project is licensed under the [Creative Commons Zero v1.0 Universal License](LICENSE).Feel free to modify and distribute the code.


## Acknowledgments

- [Google Translate API](https://cloud.google.com/translate) for providing the translation functionality.
- [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI) for the easy-to-use GUI framework.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request.


##Addition

from. steam
SmertX(Proton) 13 ноя. 2021 в 20:37
короче, я линуксист, гайд по установке. Качаем гитхаб/Valianton/Wakfu-Translate/tree/master/data => data.zip. Открываем клиент, под кнопкой "play" есть шестеренка, тыкни на нее. Под "game options" будет "game folder" нажми, клинки на "open the game folder". Пошла магия
1)открой папку "contents"
2)открой архив "data.zip"
3)в папке "contents" найди папку "i18n", в ней "i18n_en.jar" <= открой это любым архивом. Замени в ней "texts_en.properties" на тот, что был в "data.zip"
4)Вернись в папку "contents", найди папку "gui_jar", открой архивом "gui.jar", перемести из "data.zip" папку "theme"
5)Поздравляю, братик/сестренка, у тебя игра на русском спиче :csgo_ez:
