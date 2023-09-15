import os
from pyrogram import filters
from Hiroko import Hiroko, pytgcalls
from pyrogram.types import Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream




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



@Hiroko.on_message(filters.command(["play"], prefixes=["/", "!"]))
async def play(_, msg:Message):
    chat_id = msg.chat.id
    requested_by = msg.from_user.first_name
    audio = (
        msg.reply_to_message.audio or msg.reply_to_message.voice
    ) if msg.reply_to_message else None

    if audio:
           file_path = await msg.reply_to_message.download()
           await pytgcalls.join_group_call(
                  chat_id,
                  InputAudioStream(
                   file_path,),
                  stream_type=StreamType().local_stream,) 
           os.remove(file_path)
    else:
        await msg.reply("Please reply to an audio or voice message to play.")


    

@Hiroko.on_message(filters.command(["pause"], prefixes=["/", "!"]))    
async def pause(_, msg: Message):
    await pytgcalls.pause_stream(message.chat.id)
    await msg.reply_text("**» ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ɴᴏᴛʜɪɴɢ ɪs ᴘʟᴀʏɪɴɢ.**")
    


@Hiroko.on_message(filters.command(["resume"], prefixes=["/", "!"]))
async def resume(_, msg: Message):
    await pytgcalls.resume_stream(message.chat.id)
    await msg.reply_text("**» ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ sᴜᴄᴄᴇsғᴜʟʟʏ ʀᴇsᴜᴍᴇᴅ.**")
    
    


@Hiroko.on_message(filters.command(["end", "stop"], prefixes=["/", "!"]))
async def stop(_, msg: Message):    
    await pytgcalls.leave_group_call(message.chat.id)
    await msg.reply_text("**» ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ɴᴏᴛʜɪɴɢ ɪs sᴛʀᴇᴀᴍɪɴɢ.**")
    

