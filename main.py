import json

import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/joke")
async def get_joke():
    try:
        response = requests.get(
            "https://geek-jokes.sameerkumar.website/api?format=json"
        )
        if response.status_code != 200:
            return JSONResponse(
                status_code=400, content={"error": "We have an error, try again"}
            )
        return json.loads(response.content)
    except Exception as e:
        return {"error": e}
