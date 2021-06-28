from gtts import gTTS
import os

text = "dinto"
output = gTTS(text=text,lang="en",slow=True)
output.save('outpu.mp3')
os.system('start outpu.mp3')
