import requests
import openai
from Hiroko import *
from pyrogram import * 
from pyrogram.types import *
from Hiroko.Helper.database import *


ban = ["ban","spammed","rival"]
unban = ["unban","free"]
mute = ["mute","silent"]
unmute = ["unmute","speak"]
kick = ["kick", "promotion"]



text = (
"hey please don't disturb me.",
"who are you",    
"aap kon ho",
"aap mere owner to nhi lgte ",
"hey tum mera name kyu le rhe ho meko sone do",
"ha bolo kya kaam hai ",
"dekho abhi mai busy hu ",
"hey i am busy",
"aapko smj nhi aata kya ",
"leave me alone",
"dude what happend",
"?",
"nikl lwde",    
)


openai.api_key = "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"




completion = openai.Completion()


start_sequence = "\nHiroko:"
restart_sequence = "\nPerson:"
session_prompt = chatbot_txt

session = {}

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
        temperature=0.8,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3,
        stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

      

@Hiroko.on_message(filters.text, group=200)
async def chatbot_reply(hiroko :Hiroko, message):
    bot_id = (await hiroko.get_me()).id
    reply = message.reply_to_message
    if reply and reply.from_user.id == bot_id:
        q = message.text
        try:
            chat_log = session.get('chat_log')
            answer = ask(q, chat_log)
            session['chat_log'] = append_interaction_to_chat_log(Message, answer, chat_log)
            await message.reply(f"{str(answer)}", quote=True)
        except Exception as e:
            return await message.reply("I can't answer that.")        


@Hiroko.on_message(filters.command("pin"))
async def pin(_, message):
    user_id = message.reply_to_message    
    chat_id = message.chat.id    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**are you stupid how i can ban in private message**")
    elif not replied:
        await message.reply_text("whose person..")
    else:
        user_stats = await Hiroko.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:            
                await message.reply_to_message.pin()



