from fastapi import FastAPI
import uvicorn

from Natural_Language_Understanding import NLU

app = FastAPI()


@app.get('/')
def index():
    return ('Welcome to A Smart Assistant')

@app.post('/predict')
def predict(message):

    res = NLU(message)

    return res
    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1',port=8000)                        