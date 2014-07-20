import os
import datetime

def tts(text):
      return os.system("espeak -v english -s 155 -a 200 "+text+" " )