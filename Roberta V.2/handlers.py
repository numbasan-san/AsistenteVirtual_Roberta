
# handlers.py

def clean_user_google_search(user_input): # normalize input for cleaner Google search queries
    user_input = ' '.join(user_input)
    
    filter_words = [
        "que", "querer", "puedes", "dame",
        "enseñar yo", "muestra", "ver", "buscar", "busca",
        "donde", "tengo", "por", "acerca", "esto", "puedo", 
        "abre", "algo", "google"
    ]
    normalization_map = {
        "investigación": "búsqueda",
        "por": "",
        "gustar": "",
        "podrías": "",
        "puedo": "",
        "informacion": "",
        "información": ""
    }

    # convert to lowercase for consistency in filtering
    cleaned_input = user_input.lower()

    # remove filter words
    for word in filter_words:
        cleaned_input = cleaned_input.replace(word, "").strip()

    # apply normalization mappings
    for old, new in normalization_map.items():
        cleaned_input = cleaned_input.replace(old, new).strip()

    # remove any extra whitespace
    cleaned_input = ' '.join(cleaned_input.split())

    return cleaned_input

def clean_user_yt_search(user_input): # normalize input for cleaner YouTube search queries
    user_input = ' '.join(user_input)
    
    filter_words = [
        "que", "querer", "puedes", "dame",
        "enseñar yo", "muestra", "ver", "buscar", "busca",
        "donde", "tengo", "por", "acerca", "esto", "puedo", 
        "abre", "algo", "youtube"
    ]
    normalization_map = {
        "videos": "vídeos",
        "tengo": "",
        "por": "",
        "acerca": "sobre",
        "puedo": "",
    }

    # convert to lowercase for consistency in filtering
    cleaned_input = user_input.lower()

    # remove filter words
    for word in filter_words:
        cleaned_input = cleaned_input.replace(word, "").strip()

    # apply normalization mappings
    for old, new in normalization_map.items():
        cleaned_input = cleaned_input.replace(old, new).strip()

    # remove any extra whitespace
    cleaned_input = ' '.join(cleaned_input.split())

    return cleaned_input

def get_im_fine_response(): # returns a random "I'm fine" type response
    responses = [
        "Estoy bien, gracias por preguntar.",
        "Todo bien por aquí, ¿y tú?",
        "Estoy aquí para ayudarte, ¡gracias por preguntar!",
        "Me encuentro muy bien, ¿y tú?"
    ]
    return responses

def get_greetings(): # returns a list of greeting responses
    array = [
        "¡Hola! Soy Roberta, tu asistente virtual. ¿En qué puedo ayudarte hoy?",
        "¡Saludos! Soy Roberta. Estoy aquí para asistirte con lo que necesites.",
        "Hola, soy Roberta. ¿Qué información buscas?",
        "¡Hola! Soy Roberta. ¿Cómo puedo ayudarte hoy?",
        "¡Bienvenido! Soy Roberta, ¿qué deseas saber?"
    ]
    return array

def get_courteous_reply(): # returns a courteous reply
    responses = [
        "El placer es mío.",
        "Encantada de conocerte.",
        "Es un gusto para mí también.",
        "El gusto es todo mío.",
        "¡El placer es compartido!",
        "Es un honor recibir tales palabras, gracias.",
        "Muy agradecida, el placer es mutuo."
    ]
    return responses

def get_thankful_reply(): # returns a thankful reply
    replies = [
        "¡De nada! Siempre aquí para ayudarte.",
        "¡Es un placer ayudarte!",
        "No hay de qué, estoy aquí para lo que necesites.",
        "¡Con gusto! No dudes en pedirme ayuda cuando lo necesites.",
        "Para eso estoy, ¡siempre encantada de ayudarte!",
        "¡Un placer poder ayudarte!",
        "No tienes que agradecer, estoy aquí para ti.",
        "¡Con mucho gusto!",
        "Es un placer ayudarte 😊"
    ]
    return replies
