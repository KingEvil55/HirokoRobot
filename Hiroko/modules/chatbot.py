from Hiroko import Hiroko
import requests
from pyrogram import filters


api_key = "BLUE-AI-25154789-6280048819-123-white-kazu-6280048819"


def get_response(user_id, query):
    params = {
        "user_id": user_id,
        "query": query
    }
    headers = {
        "api_key": api_key
    }
    response = requests.get("https://blue-api.vercel.app/chatbot1", params=params, headers=headers)
    return response.json()



@Hiroko.on_message(filters.command("chat", prefixes="/"))
async def chatbot(client, message):
    reply = message.reply_to_message
    query = message.text.split("/chat", maxsplit=1)[1].strip()
    response = get_response(message.from_user.id, query)
    if response:
        text = response["result"]["text"]
        if not reply:
            await message.reply_text(text)
        else:
            await reply.reply_text(text)


