
# actions.py
import random, pyttsx3, pywhatkit, handlers, config
import pywhatkit.whats

NAME = 'Roberta'
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[config.languaje_voice].id)

def va_response(output): # general function to make Roberta "talk"
    if not(output == 'None' or output == None):
        print(f'{NAME}: {output}')
        talk(output)

def talk(text): # synthesizes "Roberta's voice" for responses
    engine.say(text)
    engine.runAndWait()

def im_fine(): # just random greetings
    return random.choice(handlers.get_im_fine_response())

def respond_to_greeting(): # just random greetings
    greetings = handlers.get_greetings()
    return random.choice(greetings)

def introduce_myself(): # just random self introductions
    introductions = handlers.get_introductions()
    return random.choice(introductions)

def search_youtube(query): # to look into youtube
    if query:
        query = handlers.clean_user_yt_search(query)
        message = f'Buscando "{query}" en youtube.' if config.idiom == 'es' else f'Searching for "{query}" on youtube.'
        va_response(message)
        pywhatkit.playonyt(query)
    else:
        message = "Por favor, proporciona un término de búsqueda." if config.idiom == 'es' else "Please enter a search term."
        va_response(message)

def search_google(query): # to look into google
    if query:
        query = handlers.clean_user_google_search(query)
        message = f'Buscando "{query}" en google.' if config.idiom == 'es' else f'Searching for "{query}" on google.'
        va_response(message)
        pywhatkit.search(query)
    else:
        message = "Por favor, proporciona un término de búsqueda." if config.idiom == 'es' else "Please enter a search term."
        va_response(message)

def open_whatsapp(): # to open Whatsapp
    message = f'Abriendo Whatsapp.'
    va_response(message)
    pywhatkit.whats.open_web()

def say_my_name(): # to say her name
    return f'Mi nombre es {NAME}.' if config.idiom == 'es' else f'I\'m {NAME}.'

def courteous_reply(): # to respond "nice to meet you"
    return random.choice(handlers.get_courteous_reply())

def thankful_reply(): # to say "thanks"
    return random.choice(handlers.get_thankful_reply())
