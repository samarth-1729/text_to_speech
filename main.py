from gtts import gTTS

import os

f = open('main.txt')

x = f.read()

language = 'en'

audio = gTTS(text = x, lang = language, slow = False)

audio.save("main.wav")

os.system("main.wav")
