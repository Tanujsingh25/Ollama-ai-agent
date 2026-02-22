from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from agent import handle_message

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    confirm: bool = False

@app.post("/chat")
def chat(req: ChatRequest):
    return handle_message(req.message, auto_confirm=req.confirm)

@app.get("/", response_class=HTMLResponse)
def index():
    with open("static/index.html") as f:
        return f.read()