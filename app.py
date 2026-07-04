import traceback
import models

from handlers import handle_message
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import PlainTextResponse

from config import VERIFY_TOKEN

from database import Base
from database import engine


Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.get("/")
async def home():
    return {"status": "Janaseva AI is running"}


@app.get("/webhook")
async def verify(request: Request):

    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(challenge)

    return PlainTextResponse(
        "Verification Failed",
        status_code=403
    )


@app.post("/webhook")
async def webhook(request: Request):

    body = await request.json()

    try:

        entry = body["entry"][0]
        changes = entry["changes"][0]
        value = changes["value"]
        message = value["messages"][0]

        phone = message["from"]
        text = message["text"]["body"]

        print(phone)
        print(text)

        handle_message(phone, text)

    except Exception:
        traceback.print_exc()

    return {"status": "ok"}