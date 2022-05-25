from fastapi import FastAPI
import uvicorn

import sys
import time
from pathlib import Path

module_path = str(Path.cwd() / "./")

if module_path not in sys.path:
    sys.path.append(module_path)

print(module_path)

from utils import  Kitchen , Enterainment , News , Weather , Social , IOT
from Natural_Language_Understanding import NLU

app = FastAPI()


@app.get('/')
def index():
    return ('Welcome to A Smart Assistant')

@app.post('/predict')
def predict(message):

    mappings = {'Greeting' : Social.greet,
                'Goodbye'  : Social.goodbye,
                'Thanks'   : Social.thank,
                'Joke'     : Enterainment.joke,
                'PlayMusic': Enterainment.play_music,
                'Cooking'  : Kitchen.cooking,
                'Weather'  : Weather.weather,
                'News'     : News.news,
                'Iot'      : IOT.smartHome}

    res = NLU(message)
    output = str(mappings[res['Intent']](res))
    return output 
    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1',port=8000)                        