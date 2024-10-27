
# responses.py
import random, process_requests, actions

def check_all_messages (message):
    highest_prob = {}

    def response (bot_response, list_of_words, single_response = False, required_words = []):
        nonlocal highest_prob
        highest_prob [bot_response] = process_requests.message_probability(message, list_of_words, single_response, required_words)

    response(
        lambda: actions.respond_to_greeting(), 
        ['hola', 'hello', 'salutaciones', 'buenas', 'saludo', 'saludos'], 
        single_response = True
    )
    response(
        lambda: actions.im_fine(), 
        ['cómo', 'como', 'estás', 'estás', 'vas', 'andas', 'qué tal', 'qué pasa', 'qué hay'], 
        single_response=True, 
        required_words=['cómo', 'como']  # Mantiene la palabra 'cómo' como obligatoria
    )
    response(
        lambda: actions.say_my_name(), 
        ['eres', 'nombre', 'llamas', 'tu nombre'], 
        single_response=True, 
        required_words=['quien', 'cual', 'como']
    )
    response(
        lambda: actions.courteous_reply(), 
        ['placer', 'gusto', 'conocerte', 'agradable', 'honor', 'encantado', 'mío', 'conocer'], 
        single_response=True, 
        required_words=['placer', 'conocerte']
    )
    response(
        lambda: actions.thankful_reply(),
        ['gracias', 'agradezco', 'amable', 'genial', 'ayuda', 'muchas', 'mil'],
        single_response=True,
        required_words=['gracias']
    )
    response(
        lambda: actions.open_whatsapp(),
        ['whatsapp', 'abrir', 'iniciar', 'lanzar', 'app', 'aplicación', 'conversación', 'mensaje', 'mensajes', 'comunicar', 'hablar'],
        single_response=True,
        required_words=['whatsapp']
    )
    response(
        lambda: actions.search_google(message),
        ['buscar', 'busca', 'información', 'informacion', 'consulta', 'averiguar', 'investigar', 'investiga', 'navegar', 'navega'],
        single_response=True,
        required_words=['google']
    )
    response(
        lambda: actions.search_youtube(message), 
        ['video', 'vídeo', 'vídeos', 'videos', 'buscar', 'busca', 'ver', 'contenido'], 
        single_response=True,
        required_words=['youtube']
    )
    
    best_match = max(highest_prob, key = highest_prob.get)
    return unknown () if highest_prob[best_match] < 1 else best_match()

def unknown ():
    response = [
        '¿Lo puedes repetir?', 
        "No te entiendo.", 
        "Busca en internet, quizás encuentras lo que estés buscando.", 
        "Si intentas decirme algo, creo que haces algo mal.", 
        "Si quieres que busque algo en youtube o google, recuerda especificar la página.", 
        "Por favor, reformula tu pregunta, no entiendo lo que me dices."
    ] [random.randrange(5)]

    return response
