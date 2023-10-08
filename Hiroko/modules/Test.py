import asyncio
from config import MONGO_URL
from Hiroko import Hiroko as app
from datetime import datetime, timedelta
from pyrogram import Client, filters
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from dateutil.parser import parse


mongo = MongoCli(MONGO_URL)
db = mongo.chatfight
message_collection = None

def parse_datetime(message_text):
    try:
        parsed_date = parse(message_text, fuzzy=True)
        return parsed_date
    except ValueError:
        return None

async def remember_message(user_id, chat_id, message_text):
    global message_collection
    if not message_collection:
        message_collection = db["messages"]

    timestamp = datetime.now()
    await message_collection.insert_one({
        "user_id": user_id,
        "chat_id": chat_id,
        "message_text": message_text,
        "timestamp": timestamp
    })

async def remind_users():
    global message_collection
    while True:
        if message_collection:
            current_time = datetime.now()
            timestamp_threshold = current_time - timedelta(hours=9)
            async for msg_data in message_collection.find({"timestamp": {"$lte": timestamp_threshold}}):
                user_id = msg_data["user_id"]
                chat_id = msg_data["chat_id"]
                message_text = msg_data["message_text"]
                await app.send_message(chat_id, f"Reminder for User {user_id}:\n{message_text}")
                await message_collection.delete_one({"_id": msg_data["_id"]})
        await asyncio.sleep(60)

@app.on_message(filters.command("setremember"))
async def set_reminder(_, message):
    message_text = message.text[12:].strip()
    user_id = message.from_user.id
    chat_id = message.chat.id

    parsed_datetime = parse_datetime(message_text)

    if parsed_datetime:
        await remember_message(user_id, chat_id, f"Reminder at {parsed_datetime}")
        await message.reply_text("Reminder set successfully!")
    else:
        await message.reply_text("Invalid date/time format. Please use a valid format like '13|06|2024' or 'tomorrow 9 AM'.")

@app.on_message(filters.text)
async def auto_remember_message(_, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    message_text = message.text
    await remember_message(user_id, chat_id, message_text)


