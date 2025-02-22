from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles

import app_model

app = FastAPI()

model = app_model.AppModel()

@app.get("/say")
def say_app(text: str = Query()): # 쿼리 파라미터
    response = model.get_response(text)
    return {"content":response.content}