from fastapi import FastAPI
from fastapi.params import Body
import requests


app = FastAPI()



@app.post('/siem_hook')
def hello_world(data: dict):
    url = "https://discord.com/api/webhooks/1293399469987205151/zyHHdYRLLEG7G9FtdWADwPMUj3NBWbzV1ssWfWW-hlq5MyEKmXwzAkrNivUWMx2aLK2K"

    payload = {
        "content" : f"{data}"
    }

    requests.api.post(url, payload)





if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
