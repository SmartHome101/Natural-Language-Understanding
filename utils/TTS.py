from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import pygame as pg
import os


# Authentication
url = 'https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/24d0a33f-5602-46d7-b903-a163ba991ac9'
apikey = 'kLBO4-I_XWGd3c8HrjLgzE-IcxIvGg_eWp0rbXK65myX'

#setup service
authenticator = IAMAuthenticator(apikey)
#new TTS service
tts = TextToSpeechV1(authenticator=authenticator)
#set service URL
tts.set_service_url(url)



num = 0
def speak(output):
    global num
    # num to rename every audio file with different name to remove ambiguity
    num += 1
    
    file = str(num)+'.mp3'
    with open(file, 'wb') as audio_file:
        res = tts.synthesize(output, accept='audio/mp3', voice='en-US_MichaelV3Voice').get_result()
        audio_file.write(res.content)    
        
    # for playing note.mp3 file
    path = "./"
    pg.mixer.init()
    sound = pg.mixer.Sound(path + file)
    sound.play()
    os.remove(path + file)          
   