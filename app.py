from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()



@app.post('/siem_hook')
def hello_world(payload: dict):
    return payload



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)

