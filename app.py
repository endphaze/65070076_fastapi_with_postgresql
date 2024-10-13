from fastapi import FastAPI
from fastapi.params import Body
import requests
import json
from dotenv import load_dotenv, dotenv_values
import os

app = FastAPI()


load_dotenv()


@app.post('/siem_hook')
def hello_world(data: dict):
    url = os.environ.get("discord_webhook_url") 

    json_obj = json.dumps(data, indent=4)
    payload = {
        'content' : f'```json\n{json_obj}```'
    }

    requests.api.post(url, payload)
    




if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)

