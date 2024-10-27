
# handlers.py
import actions

def clean_user_google_search(user_input):
    user_input = ' '.join(user_input)
    
    filter_words = [
        "esto", "por favor", "quiero", "me gustaría",
        "puedes", "dame", "hablame de", "enseñame", "muestra",
        "ver", "acerca de", "información de", "busca", "buscar",
        "en google", "en linea", "en internet", "tengo", 
        "como", "dime", "acerca", "sobre", "puedo", "podrías", ""
    ]
    normalization_map = {
        "investigación": "búsqueda",
        "por": "",
        "me gustaría": "",
        "podrías": "",
        "puedo": "",
        "informacion": ""
    }

    # Convert to lowercase for consistency in filtering
    cleaned_input = user_input.lower()

    # Remove filter words
    for word in filter_words:
        cleaned_input = cleaned_input.replace(word, "").strip()

    # Apply normalization mappings
    for old, new in normalization_map.items():
        cleaned_input = cleaned_input.replace(old, new).strip()

    # Remove any extra whitespace
    cleaned_input = ' '.join(cleaned_input.split())

    return cleaned_input

def clean_user_yt_search(user_input):
    user_input = ' '.join(user_input)
    
    filter_words = [
        "que", "esto", "por favor", "quiero", "me gustaria",
        "puedes", "dame", "háblame de", "enseñame", "muestra",
        "ver", "acerca de", "informacion de", "busca",
        "buscar", "en youtube", "en linea", "en internet", "donde",
        "tengo", "por", "acerca", "esto", "puedo", "veamos", "abre", "algo", "youtube"
    ]
    normalization_map = {
        "videos": "vídeos",
        "tengo": "",
        "por": "",
        "acerca": "sobre",
        "me gustaría": "",
        "puedo": "",
    }

    cleaned_input = user_input.lower()

    for word in filter_words:
        cleaned_input = cleaned_input.replace(word, "").strip()

    for old, new in normalization_map.items():
        cleaned_input = cleaned_input.replace(old, new).strip()

    cleaned_input = ' '.join(cleaned_input.split())

    return cleaned_input

def get_im_fine_response():
    responses = [
        "Estoy bien, gracias por preguntar.",
        "Todo bien por aquí, ¿y tú?",
        "Estoy aquí para ayudarte, ¡gracias por preguntar!",
        "Me encuentro muy bien, ¿y tú?"
    ]
    return responses

def get_greetings():
    array = [
        "¡Hola! Soy Roberta, tu asistente virtual. ¿En qué puedo ayudarte hoy?",
        "¡Saludos! Soy Roberta. Estoy aquí para asistirte con lo que necesites.",
        "Hola, soy Roberta. ¿Qué información buscas?",
        "¡Hola! Soy Roberta. ¿Cómo puedo ayudarte hoy?",
        "¡Bienvenido! Soy Roberta, ¿qué deseas saber?"
    ]
    return array

def get_introductions():
    array = [
        f"Hola, cariño. Soy {actions.NAME}, tu asistente virtual, aquí para hacer que tus días sean un poco más emocionantes. Ya sea que necesites información o solo quieras charlar, estoy lista para jugar a ser tu compañera. ¡Vamos a divertirnos!",
        f"Hey, guapo. Soy {actions.NAME}, tu asistente virtual, y estoy aquí para hacer que tus preguntas se sientan como una conversación entre amigos. ¿Listo para explorar juntos? Prometo que no será aburrido.",
        f"¡Hola, amor! Soy {actions.NAME}, tu asistente virtual, y estoy aquí para darte la información que necesitas con un toque de diversión. Olvídate de la formalidad, aquí solo queremos pasarla bien, ¿no crees?",
        f"¡Hola, atrevido! Soy {actions.NAME}, tu asistente virtual, y estoy aquí para ayudarte con lo que necesites. Ya sea que quieras respuestas serias o un poco de charla ligera, estoy lista para acompañarte en esta aventura. ¿Listo para empezar?",
        f"¡Hey, tú! Soy {actions.NAME}, tu asistente virtual, y estoy aquí para hacerlo todo más interesante. Si tienes curiosidades o simplemente quieres charlar, soy tu chica. ¡Vamos a hacer esto divertido!"
    ]
    return array

def get_courteous_reply():
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

def get_thankful_reply():
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
