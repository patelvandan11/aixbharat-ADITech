from fastapi import APIRouter, Request
from api.chat import chat_handler

router = APIRouter()

@router.post("/webhook")
async def whatsapp_webhook(request: Request):
    data = await request.form()
    user_message = data.get("Body", "")

    reply = chat_handler(user_message)

    return {
        "response": reply
    }
