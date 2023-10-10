import pyttsx3
import openai
from dotenv import load_dotenv
import speech recognition as sr 
from googletrans import Translator 






def Listen():
    r = sr.Recognizer()  # Create a recognizer object

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 8, 8)  # Listening Mode.....

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="hi")
    except:
        return ""

    query = str(query).lower()
    return query



def Trans(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print("You: ", data)
    return data
  


def speak(text):
    text_real = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    print("")
    print(f"> Hiroko: {text_real}")
    print("")
    engine.say(text_real)
    engine.runAndWait()
     



openai.api_key = "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"
load_dotenv()

completion = openai.Completion()



def ReplyBrain(question, chat_log=None):

    file_log = open("chat_log.txt", "r")
    chat_log_template = file_log.read()
    file_log.close()

    if chat_log is None:
        chat_log = chat_log_template
    
    prompt = f"You: {question}\nJarvis:"

    response = completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=68,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0
    )
    answer = response.choices[0].text.strip()

    chat_log_template_update = chat_log_template + f"\nYou: {question}\nHiroko: {answer}"
    file_log = open("chat_log.txt", "w")
    file_log.write(chat_log_template_update)
    file_log.close()

    return answer



def MicExecution():
    query = Listen()
    data = Trans(query)
    x = ReplyBrain(data)
    return x








