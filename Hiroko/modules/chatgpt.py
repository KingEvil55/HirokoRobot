import time
from pyrogram import Client, filters
import openai
from Hiroko import Hiroko
from pyrogram.enums import ChatAction, ParseMode





openai.api_key = "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"




@Hiroko.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(hiroko :Hiroko, message):
    
    try:
        start_time = time.time()
        await hiroko.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "**ʜᴇʟʟᴏ sɪʀ**\n**ᴇxᴀᴍᴘʟᴇ:-**`.ask How to set girlfriend ?`")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            await message.reply_text(f"{x}")     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ**: {e} ")        


import time
from pyrogram import Client, filters
import openai
from gtts import gTTS
import io
from Hiroko import Hiroko, pytgcalls
from pyrogram.enums import ChatAction
from pytgcalls.types.input_stream import InputStream
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped


@Hiroko.on_message(filters.command(["peest"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(hiroko: Hiroko, message):
    
    try:
        start_time = time.time()
        await hiroko.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text("ʜᴇʟʟᴏ sɪʀ\nᴇxᴀᴍᴘʟᴇ:-.ask How to set girlfriend ?")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL, messages=[{"role": "user", "content": a}], temperature=0.2)
            x = resp['choices'][0]["message"]["content"]
            
            # Convert the AI response to audio
            tts = gTTS(text=x, lang='en', slow=False)
            audio_stream = io.BytesIO()
            tts.save(audio_stream)
            audio_stream.seek(0)
            
            # Save audio file to path
            audio_file_path = 'response.mp3'
            with open(audio_file_path, 'wb') as f:
                f.write(audio_stream.getbuffer())
            
            # Send the audio to the voice chat
            chat_id = message.chat.id
            
            await pytgcalls.join_group_call(
                message.chat.id, 
                InputStream(
                    AudioPiped(audio_file_path),
                ),
                stream_type=StreamType().local_stream,
            )
            await message.reply_text("chat gpt answering..")
            
    except Exception as e:
        await message.reply_text(f"ᴇʀʀᴏʀ: {e}")


                                                                      
