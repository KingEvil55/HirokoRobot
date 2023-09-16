import os, asyncio
from config import OWNER_ID
from pyrogram import filters
from Hiroko import Hiroko, pytgcalls, userbot
from pyrogram.types import Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import AudioPiped




@Hiroko.on_message(filters.video_chat_started)
async def brah(_, msg):
       await msg.reply("voice chat started")

@Hiroko.on_message(filters.video_chat_ended)
async def brah2(_, msg):
       await msg.reply("voice chat ended")

@Hiroko.on_message(filters.video_chat_members_invited)
async def fuckoff(hiroko :Hiroko, message:Message):
           text = f"{message.from_user.mention} Invited "
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} 😉")
           except:
             pass


@Hiroko.on_message(filters.command("join"))
async def join_userbot(_,msg:Message):
  chat_id = msg.chat.id
  invitelink = await Hiroko.export_chat_invite_link(chat_id)
  await userbot.join_chat(invitelink)
  await msg.reply("assistant successfully join.")




@pytgcalls.on_stream_end()
async def on_stream_end(_,msg:Message):
    await pytgcalls.leave_group_call(msg.chat.id)
    


@Hiroko.on_message(filters.command(["play"], prefixes=["/", "!"]))
async def play(_, msg: Message):
    chat_id = msg.chat.id
    requested_by = msg.from_user.first_name
    audio = msg.reply_to_message.audio or msg.reply_to_message.voice if msg.reply_to_message else None

    if audio:
        file_path = await msg.reply_to_message.download()
        x = await pytgcalls.join_group_call(chat_id, AudioPiped(file_path), stream_type=StreamType().local_stream)
        os.remove(file_path)
        sum = await msg.reply_text(f"ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ\n\n0% ▓▓▓▓▓▓▓▓▓▓▓▓ 100%")  
        await asyncio.sleep(0.5)   
        try:
            if x:
                await sum.edit_text(f"Now playing song\nRequested by {requested_by}")
        except UserAlreadyParticipant:
            pass
        except Exception as e:
            print(e)             
        await msg.reply(f"Sorry {msg.from_user.mention}, please wait until the current song ends.")
    else:
        await msg.reply("Please reply to an audio or voice message to play.")




@Hiroko.on_message(filters.command(["pause"], prefixes=["/", "!"]))    
async def pause(_, msg: Message):
    chat_id = msg.chat.id
    if str(chat_id) in str(pytgcalls.active_calls):
        await pytgcalls.pause_stream(chat_id)
        await msg.reply(f"Music player successfully paused\nPaused by {msg.from_user.mention}")
    else:
        await msg.reply(f"Sorry {msg.from_user.mention}, I can't pause because there is no music playing on the voice chat.")


@Hiroko.on_message(filters.command(["resume"], prefixes=["/", "!"]))    
async def resume(_, msg: Message):
    chat_id = msg.chat.id
    if str(chat_id) in str(pytgcalls.active_calls):
        await pytgcalls.resume_stream(chat_id)
        await msg.reply(f"Music player successfully resumed\nResumed by {msg.from_user.mention}")
    else:
        await msg.reply(f"Sorry {msg.from_user.mention}, I can't resume because there is no music playing on the voice chat.")


@Hiroko.on_message(filters.command(["end"], prefixes=["/", "!"]))    
async def stop(_, msg: Message):
    chat_id = msg.chat.id
    if str(chat_id) in str(pytgcalls.active_calls):
        await pytgcalls.leave_group_call(chat_id)
        await msg.reply(f"Music player successfully ended\nEnded by {msg.from_user.mention}")
    else:
        await msg.reply(f"Sorry {msg.from_user.mention}, I can't end music because there is no music playing on the voice chat.")


