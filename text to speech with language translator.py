# -*- coding: utf-8 -*-
"""
Created on Sun May 31 14:23:40 2020

@author: Aaditree Jaisswal
"""

from gtts import gTTS
import os
import goslate

mytext=input("Enter text :")


gs = goslate.Goslate()

list = input("Choose Language :")

translatedText = gs.translate(mytext,list)

speed = input("SPEED? slow or fast")
if(speed=="slow"):
    speed=False
else:
    speed=True

output = gTTS(text = translatedText,lang=list,slow=speed)

output.save("output.mp3")

os.system("start output.mp3")